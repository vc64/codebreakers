import random
import requests
import re

# todo
# look into where to get quotes, maybe litquotes
# make sure to filter out quotes that are too short
# maybe just use quotes from specific people, avoids potential content issues
# good quote sources
#   jane austen
#   isaac asimov

# Bartlett's familiar quotations - book


def findQuotesLit(html):
    return re.findall("div>\s+\"?([\.a-zA-Z0,!?;:\' ]+?)\"?\n[\s\S]*", html)

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

print(getQuotesLit(["Life"]))



