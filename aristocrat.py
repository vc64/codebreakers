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
    return re.findall("div>\n([\s\S]*)\n", html)
# ~ <i>.*</i>\nby<[\s\S]+>(.+)</a>
def getQuotesLit(topicList):
    for topic in topicList:
        link = "https://www.litquotes.com/quote_topic_resp.php?QuoteType=" + topic
        f = requests.get(link)
        html = f.text

        print(html)
        print(findQuotesLit(html))

getQuotesLit(["Autumn"])



