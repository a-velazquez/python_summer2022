#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 2

Created on Fri Aug 12 15:55:14 2022

@author: Alma Velazquez
"""

from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import time
import csv

biden_speeches = {
    "date": [],
    "title": [],
    "full_text": [],
    "endnotes": [],
}


top_link = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=01-20-2021&to%5Bdate%5D=&person2=200320&category2%5B0%5D=8&items_per_page=100"
top_page = urllib.request.urlopen(top_link)

soup = BeautifulSoup(top_page.read())

soup.find_all("h3")
soup.find_all("div", {"class": "view-header"})


def scrape_results_page(web_address):

    web_page = urllib.request.urlopen(web_address)

    speech_soup = BeautifulSoup(web_page.read())

    all_dates = speech_soup.find_all(
        "td",
        {
            "class": "views-field views-field-field-docs-start-date-time-value text-nowrap"
        },
    )

    biden_speeches["date"] = [date.text.replace("\n", "").strip() for date in all_dates]

    all_titles = speech_soup.find_all("td", {"class": "views-field views-field-title"})

    biden_speeches["title"] = [
        title.text.replace("\n", "").strip() for title in all_titles
    ]

    txt_links = [
        "https://www.presidency.ucsb.edu" + title.find_all("a")[0]["href"]
        for title in all_titles
    ]

    for link in txt_links:

        page = urllib.request.urlopen(link)

        temp_soup = BeautifulSoup(page.read())

        content = temp_soup.find_all("div", {"class": "field-docs-content"})

        txt = ""
        for line in content:
            txt += line.text.replace("\n", " ").strip()

        biden_speeches["full_text"].append(txt)

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

        biden_speeches["endnotes"].append(endnotes)

        time.sleep(random.uniform(1, 8))
        print("Pause Ended")


with open("biden_speeches.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(biden_speeches.keys())
    writer.writerows(zip(*biden_speeches.values()))
