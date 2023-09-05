from bs4 import BeautifulSoup
import requests

url = "https://www.healthline.com/nutrition/50-super-healthy-foods"

source = requests.get(url).text

with open("templates/healthline.html", "w", encoding="utf-8") as file:
    file.write(source)
