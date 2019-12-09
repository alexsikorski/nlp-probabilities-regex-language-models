import os
import re
from urllib import request

from bs4 import BeautifulSoup
from greenery import lego, fsm


# QUESTION 2
testUrl = "https://fakenumber.org/united-kingdom"

testText = """FORMATS IN ASSIGNMENT QUESTION
+55 51 33083838
1206 872020
01206 872020
05679401945
+44 5679401945
0044 5679401945

UK FORMATS
+447222555555
447429006370
+44 7222 555 555
(0722) 5555555
"""


# Definition for processing a url
def processUrl(url):
    rawText = BeautifulSoup((request.urlopen(url).read().decode("utf8")), "html.parser")
    return rawText


# Definition for processing numbers
def outputNumbers(context):
    for a in re.findall(
            r'(\+\d{2}\s?\d{4}|\+\d{2}\s\d{2}\s\d{2}|\(?\d{4}\)?|\d{5})(\s\d{10}|\d{8}|\s?\d{7}|\s?\d{3}\s?\d{3})',
            str(context)):
        print("Found a match!")
        # FORMATTING
        output = a[0] + a[1]  # combines both together to form one string
        output = output.replace(" ", "")  # replaces spaces with nothing, essentially removing them
        output = output.replace(")", "")
        output = output.replace("(", "")  # replaces brackets with nothing
        if output[0] and output[1] == "0" and len(output) == 14:  # if first two strings == 0 and the length is
            # greater than 14...
            output = output[2:]  # replaces two "0"s at start of string with empty field
        if len(output) == 10:
            output = "0" + output  # if the number is missing a 0 at the start (10 digit and not 11)
        if len(output) == 12:  # number with area code but without + sign
            output = "+" + output
        print("Telephone: " + output)
        print()


# Loop for interface
print("Question 3")
while True:
    userInput = int(input("""
MAIN MENU (Phone Number Finder)
Enter (1) to view test string with required formats...
Enter (2) to find UK numbers in test string...
Enter (3) to view test url...
Enter (4) to find UK numbers in test url...
Enter (5) to find UK numbers in given url...
Enter (0) to exit and view Question 4...
"""))
    if userInput == 0:
        print()
        print("Have a nice day!")
        break

    if userInput == 1:
        print()
        print(testText)
        print()

    if userInput == 2:
        outputNumbers(testText)

    if userInput == 3:
        print("Test URL: " + testUrl)

    if userInput == 4:
        outputNumbers(processUrl(testUrl))

    if userInput == 5:
        userUrl = str(input("Please enter url: "))
        outputNumbers(processUrl(userUrl))

# QUESTION 4
print("""
Question 4
""")
lego.lego  # instance of lego
fsm.fsm  # instance of fsm
string = "(\+\d{2}\s?\d{4}|\+\d{2}\s\d{2}\s\d{2}|\(?\d{4}\)?|\d{5})(\s\d{10}|\d{8}|\s?\d{7}|\s?\d{3}\s?\d{3})"  # sets
# variable string to the regular expression

lego1 = lego.parse(string)  # creates lego object after parsing string
print(lego1.to_fsm())  # prints finite state machine
