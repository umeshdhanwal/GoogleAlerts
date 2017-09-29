import feedparser
d = feedparser.parse('https://www.google.com/alerts/feeds/03052694921060148104/10484262279899711572')
for e in d.entries:
     print(e.title)
     print(e.link)
     print(e.description)
     print("\n") # 2 newlines
