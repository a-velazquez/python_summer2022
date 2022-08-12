import re
import os

os.chdir("./Lab")


# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
    obama = f.readlines()

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

pattern = r"^((?!the).)*$"

for l in obama:
    if re.search(pattern, l):
        print(l)
# should have 86

# TODO: print lines that contain a word of any length starting with s and ending with e

pattern2 = r"\bs\S*e\b"


for l in obama:
    if re.search(pattern2, l):
        print(l)

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = "Please enter a date in the following format: 08.18.21"


labs = ["Month:", "Day:", "Year:"]

date_pattern = r"(\d{2}\.\d{2}\.\d{2})"

date = re.findall(pattern, date)[0]

date_parts = re.split(r"\.", date)

for l, d in zip(labs, date_parts):
    print(l, d)
