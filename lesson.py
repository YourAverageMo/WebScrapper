import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.findAll(name="span", class_="titleline")

article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [
    score.getText() for score in soup.findAll(name="span", class_="score")
]

# split = article_upvotes[0].split()
article_upvotes = [int(score.split()[0]) for score in article_upvotes]
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# with open("./website.html") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")
# tags = soup.findAll(name="a")

# for tag in tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)

# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select(".heading")
# print(heading)