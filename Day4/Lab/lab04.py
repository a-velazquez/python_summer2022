## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence.
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page

from bs4 import BeautifulSoup
import urllib.request
import csv

web_address = "https://polisci.wustl.edu/people/88/"
web_page = urllib.request.urlopen(web_address)
web_page  # stored on machine

# Parse it
soup = BeautifulSoup(web_page.read())
print(soup.prettify())

all_a_tags = soup.find_all("a")

professor_pages = []
for i in range(0, len(all_a_tags)):
    page_link = web_address[:-10] + all_a_tags[i]["href"][1:]
    professor_pages.append(page_link + "/")

for i, link in enumerate(professor_pages):
    print(i, link)

print(professor_pages[19:42])

professor_pages = professor_pages[19:42]

prof_info = {"names": [], "specializations": [], "title": [], "emails": [], "links": []}

for link in professor_pages:
    try:
        # web page
        prof_info["links"].append(link)
        page = urllib.request.urlopen(link)
        prof_soup = BeautifulSoup(page.read())

        # name
        all_h1_tags = prof_soup.find_all("h1")
        prof_info["names"].append(all_h1_tags[0].text.strip())

        # title
        all_title_tags = prof_soup.find_all("div", {"class": "title"})
        prof_info["title"].append(list(all_title_tags[0].stripped_strings))

        # interests
        all_interest_uls = prof_soup.find_all("ul", {"class": "interests"})
        interest_list = []
        for ul in all_interest_uls:
            for li in ul.findAll("li"):
                interest_list.append(li.text.strip())
        prof_info["specializations"].append(interest_list)

        # emails
        all_emails_tags = prof_soup.find_all("ul", {"class": "detail contact"})
        for ul in all_emails_tags:
            for li in ul.findAll("li"):
                a_links = li.find_all("a")
                for i in range(len(a_links)):
                    if "mailto" in a_links[i]["href"]:
                        prof_info["emails"].append(
                            a_links[i]["href"].replace("mailto:", "")
                        )
    except:
        print(link)
        pass

with open("professor_info.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(prof_info.keys())
    writer.writerows(zip(*prof_info.values()))
