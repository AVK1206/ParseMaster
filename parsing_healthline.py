from bs4 import BeautifulSoup
import requests

url = "https://www.healthline.com/nutrition/50-super-healthy-foods"

source = requests.get(url).text

with open("templates/healthline.html", "w", encoding="utf-8") as file:
    file.write(source)

with open("templates/healthline.html", encoding="utf-8") as file:
    source = file.read()

soup = BeautifulSoup(source, "lxml")
title = soup.title
print(title.text)

# To get urls with the appropriate text in a class what we need
links_in_class_css_6kcp84 = soup.find(class_="css-6kcp84").find("ul").find_all("a")
print(*(f"{' '. join(info.text.split())}: {info.get('href')})" for info in links_in_class_css_6kcp84 if
        info.get('href') and info.get('href').startswith('https')), sep="\n")

# To find only unique text in all spans
span_all = soup.find_all("span")
print(*set((span.text.strip() for span in span_all)), sep="\n")


text_in_class_css_12we7vs = soup.find(class_="css-12we7vs").find_all("li")
print(*(str(text_in.text).split() for text_in in text_in_class_css_12we7vs))
#
text_in_p_in_article_css_d2znx6 = soup.find(class_="article-body css-d2znx6 undefined").find_all("p")
print(*(" ".join(elem.text.split()) for elem in text_in_p_in_article_css_d2znx6), sep="\n")

healthy_fruits_in_article_css_d2znx6 = soup.find(class_="article-body css-d2znx6 undefined").find_all("h3")
print(*(" ".join(elem.text.split()) for elem in healthy_fruits_in_article_css_d2znx6), sep="\n")

