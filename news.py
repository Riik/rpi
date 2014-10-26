import feedparser
def get_news():
    url = 'http://www.volkskrant.nl/rss.xml'
    feed = feedparser.parse(url)
    #for item in feed["items"]:
    #    title = item["title"].encode('ascii','replace')
    #    print(len(title))
    title = feed["items"][0]["title"].encode('ascii','replace')
    print(title)
    # split title in two parts with max length 16, without breaking words
    i = 16
    while title[i] != ' ':
        i = i - 1
    k = i + 16
    if k < len(title):
	while title[k] != ' ':
            k = k - 1
    else:
	k = len(title)
    t = []
    t.append(title[:i])
    t.append(title[i:k])
    return t
    
get_news()
