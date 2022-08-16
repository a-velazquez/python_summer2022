#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 2

Created on Fri Aug 12 15:55:14 2022

@author: Alma Velazquez
"""

from bs4 import BeautifulSoup
import urllib.request
from datetime import date
import random
import time
import csv
import re


"""Generates a csv containing Joe Biden's spoken addresses 
and remarks from January 20th, 2021 through run date."""


# extract and store current date
today = str(date.today().strftime("%m-%d-%Y"))

# define search query link, using today's date
top_link = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=01-20-2021&to%5Bdate%5D={today}&person2=200320&category2%5B0%5D=8&items_per_page=100"
top_page = urllib.request.urlopen(top_link)

# extract and store number of results returned
soup = BeautifulSoup(top_page.read())
h3 = soup.find_all("h3")

# this will always be the last group of digits under the third h3 tag
results = int(re.findall(r"\d+", h3[2].text)[-1])

# use number of results to determine number of pages to iterate over
if results % 100 != 0:

    pages = (results // 100) + 1
else:

    pages = results // 100


def get_speech_links(web_address):
    """Given the url for a page of search results, 
    return a list of links to each speech page."""

    web_page = urllib.request.urlopen(web_address)

    speech_soup = BeautifulSoup(web_page.read())

    all_titles = speech_soup.find_all("td", {"class": "views-field views-field-title"})

    txt_links = [
        "https://www.presidency.ucsb.edu" + title.find_all("a")[0]["href"]
        for title in all_titles
    ]

    return txt_links


def scrape_speech(link):
    """Extract relevant information given url for an individual speech. 
    Returns a single dictionary."""

    # instantiate empty dict
    speech = {}

    page = urllib.request.urlopen(link)

    temp_soup = BeautifulSoup(page.read())

    speech["date"] = temp_soup.find_all("span", {"class": "date-display-single"})[
        0
    ].text

    # speech title is systematically first h1 tagged item
    speech["title"] = temp_soup.find_all("h1")[0].text

    content = temp_soup.find_all("div", {"class": "field-docs-content"})

    # add each line of speech to empty string
    txt = ""
    for line in content:
        txt += line.text.replace("\n", " ").strip()

    speech["full_text"] = txt

    # extract and store any footnotes and citations
    notes = temp_soup.find_all("div", {"class": "field-docs-footnote"})
    cites = temp_soup.find_all("div", {"class": "field-prez-document-citation"})

    # instantiate empty string of endnotes, will combine both footnotes and citations
    endnotes = ""
    if len(notes) != 0:
        for note in notes:
            endnotes += note.text.replace("\n", " ").strip()
    else:
        # account for speeches with no footnotes
        endnotes += "No footnotes"

    # separate footnotes and citations with a line break
    endnotes += " /n "

    if len(cites) != 0:
        for cite in cites:
            endnotes += cite.text.replace("\n", " ").strip()
    else:
        # account for speeches with no citations
        endnotes += "No citations"

    speech["endnotes"] = endnotes

    # sleep between 1 and 5 seconds after scraping the speech
    time.sleep(random.uniform(1, 4))

    return speech


# generate csv file for all results of a search
with open("biden_speeches.csv", "w") as outfile:
    # instantiate writer
    w = csv.DictWriter(outfile, fieldnames=("date", "title", "full_text", "endnotes"))
    # write csv header
    w.writeheader()

    # instantiate page and speech counters
    pg = 1
    speech = 1

    # iterate over search result pages
    for i in range(0, pages):

        # print informative message
        print(f"Now on results page {pg} out of {pages}")

        # account for first page of results
        if i == 0:
            results_page = top_link
        else:
            results_page = top_link + f"&page={i}"

        # use get links function to get speech links from this page of results
        text_links = get_speech_links(results_page)

        # iterate over speeches
        for l in text_links:

            # print informative message
            print(f"Now on speech {speech} out of {results}")

            # write each speech's info to the csv
            w.writerow(scrape_speech(l))

            speech += 1

        pg += 1
