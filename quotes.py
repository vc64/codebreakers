import random
import requests
import re
import string

# todo
# look into where to get quotes, maybe litquotes
# make sure to filter out quotes that are too short
# maybe just use quotes from specific people, avoids potential content issues
# good quote sources
#   jane austen
#   isaac asimov

# Bartlett's familiar quotations - book


def findQuotesLit(html):

    # string.punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    accepted_punctuation = "!\"&'(),-./:;?\_`"
    pattern = "div>\s+\"?([\.a-zA-Z" + accepted_punctuation + " ]+?)\"?\n[\s\S]*?by <.+>([\w" + accepted_punctuation + " ]+)<"

    return re.findall(pattern, html)

    # trying to get author but it isnt working for all quotes
    #  by <.+>([\w ]+)<


    # "div>\n\"?(.+)\"?\n"
# ~ <i>.*</i>\nby<[\s\S]+>(.+)</a>


def getQuotesLit(topicList):
    quotes = []

    for topic in topicList:
        link = "https://www.litquotes.com/quote_topic_resp.php?QuoteType=" + topic
        f = requests.get(link)
        html = f.text

        # print(html)

        quotes.append(findQuotesLit(html))

    return quotes

print(len(getQuotesLit(["Life"])[0]))

# todo
# get the total number of quotes per topic and 
#       use that to judge how many pages of quotes 
#       can be taken
# 
# filter based on quote length
# save locally to avoid issues if website changes or etc



