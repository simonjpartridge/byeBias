import requests
from bs4 import BeautifulSoup


html_page = requests.get("http://www.allsides.com")
soup = BeautifulSoup(html_page.text, "lxml")


# Obtaining articles links
news_links = soup.findAll("div", { "class" : "news-title" })

links = []
for link in news_links:
    links.append(link.find('a')['href'])


# Obtaining article text
# articles = []
#
# for link in links:
#     html_page = requests.get(link)
#     soup = BeautifulSoup(html_page.text, "lxml")
#     paragraphs = soup.findAll('p')
#
#     article = ""
#     for p in paragraphs:
#         article = article + p.text
#
#     articles.append(article)
#
#
# print(articles)


# Obtaining articles labels
news_labels = soup.findAll("div", { "class" : "bias-image" })

labels = []

for label in news_labels:
    image_name = label.find('img')['src']
    image_name = image_name.split("/")[-1]
    image_name = image_name.split(".")[0]
    labels.append(image_name)


# print(labels)
