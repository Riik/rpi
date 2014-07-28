import feedparser
url = 'http://feeds.nos.nl/nosjournaal?format=xml'
feed = feedparser.parse(url)
for item in feed["items"]:
    x = item["title"]
    x = x.encode('ascii','replace')
    print(len(x))