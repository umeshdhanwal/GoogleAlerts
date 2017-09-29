import feedparser
d = feedparser.parse('https://www.google.com/alerts/feeds/14273445301609542014/5918640904071536250')
for e in d.entries:
     print(e.title)
     print(e.link)
     print(e.description)
     print("\n") # 2 newlines
