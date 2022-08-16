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


today = str(date.today().strftime("%m-%d-%Y"))

top_link = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=01-20-2021&to%5Bdate%5D={today}&person2=200320&category2%5B0%5D=8&items_per_page=100"
top_page = urllib.request.urlopen(top_link)

soup = BeautifulSoup(top_page.read())

h3 = soup.find_all("h3")

results = int(re.findall(r"\d+", h3[2].text)[-1])

# number of pages to iterate over
if results % 100 != 0:

    pages = (results // 100) + 1

else:

    pages = results // 100


def advance_page(web_address):
    """Docstring"""

    web_page = urllib.request.urlopen(web_address)

    speech_soup = BeautifulSoup(web_page.read())

    all_titles = speech_soup.find_all("td", {"class": "views-field views-field-title"})

    txt_links = [
        "https://www.presidency.ucsb.edu" + title.find_all("a")[0]["href"]
        for title in all_titles
    ]

    return txt_links


def scrape_results_page(link):
    """Docstring"""

    speech = {}

    page = urllib.request.urlopen(link)

    temp_soup = BeautifulSoup(page.read())

    speech["date"] = temp_soup.find_all("span", {"class": "date-display-single"})[
        0
    ].text

    speech["title"] = temp_soup.find_all("h1")[0].text

    content = temp_soup.find_all("div", {"class": "field-docs-content"})

    txt = ""
    for line in content:
        txt += line.text.replace("\n", " ").strip()

    speech["full_text"] = txt

    notes = temp_soup.find_all("div", {"class": "field-docs-footnote"})
    cites = temp_soup.find_all("div", {"class": "field-prez-document-citation"})

    endnotes = ""
    if len(notes) != 0:
        for note in notes:
            endnotes += note.text.replace("\n", " ").strip()
    else:
        endnotes += "No footnotes"

    endnotes += " /n "

    if len(cites) != 0:
        for cite in cites:
            endnotes += cite.text.replace("\n", " ").strip()
    else:
        endnotes += "No citations"

    speech["endnotes"] = endnotes

    time.sleep(random.uniform(1, 5))

    return speech


with open("biden_speeches.csv", "w") as outfile:
    w = csv.DictWriter(outfile, fieldnames=("date", "title", "full_text", "endnotes"))
    w.writeheader()

    pg = 0
    speech = 0

    for i in range(0, pages):

        print(f"Now on results page {pg} out of {pages}")

        if i == 0:
            results_page = top_link
        else:
            results_page = top_link + f"&page={i}"

        text_links = advance_page(results_page)

        for l in text_links:

            print(f"Now on speech {speech} out of {results}")

            w.writerow(scrape_results_page(l))

            speech += 1

        pg += 1
