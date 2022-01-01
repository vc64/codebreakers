import random
import requests
import re
import string
import math

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
    # accepted_punctuation = "!\"#&'(),-./:;?\_`"
    accepted_punctuation = string.punctuation
    # pattern = "div>\s+\"?([\s\S]+?)\"?\n[\s\S]*?by <.+>([\s\S]+?)<"

    pattern = "div>\s+\"?([^<>\\\\]{85,})\"?\n* ~[\s\S]*?by <A.+?>([\s\S]+?)<"
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

        numQuotes = int(re.findall(">(\d+).+?Quotes from Literature", html)[0])

        for i in range(1, math.ceil(numQuotes/10)+1):
            # print(i)
            link = "https://www.litquotes.com/quote_topic_resp.php?QuoteType=" + topic + "&page=" + str(i)
            f = requests.get(link)
            html = f.text
            quotes.append(findQuotesLit(html))

    return quotes

topic_list = ["Life", "Death", "Autumn", "Winter"]

print([len(x) for x in getQuotesLit(topic_list)])
# print(getQuotesLit(["Life"])[0])
# print(getQuotesLit(["Life"])[1])

# todo
# save locally to avoid issues if website changes or etc

