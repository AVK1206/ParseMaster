import re

from bs4 import BeautifulSoup

with open("templates/main_page.html") as file:
    source = file.read()

soup = BeautifulSoup(source, "lxml")

title = soup.title.text
print(title)

# To find the first text in tag h1
main_page_h1 = soup.find("h1")
# print(main_page_h1.text)

# To find the text in all tag h1
main_page_all_h1 = soup.find_all("h1")
print(*[item.text for item in main_page_all_h1], sep="\n")

# To find the text in specific span
specific_user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).text.strip()
print(specific_user_name)

user_info_all_spans = soup.find(class_="user__info").find_all("span")

# Get all spans besides the text "Mrs Anna" inside
filtered_span = filter(lambda span: span.text != "Mrs Anna", user_info_all_spans)
print(*[info.text for info in filtered_span], sep="   ")

social_links = soup.find(class_="social__networks").find("ul").find_all("a")
print(*(f"{info.text}: {info.get('href')}" for info in social_links), sep="\n")

# Get info using find parents
post_divs = soup.find(class_="post__text").findParents("div", "user__post")
print(*(info.text.strip() for info in post_divs))

# Next.element
next_element = soup.find(class_="post__title").next_element.next_element.text.strip()
print(next_element)

# Previous element
previous_element = soup.find(class_="post__text").previous_element.previous_element.text.strip()
print(previous_element)

# Next siblings
next_sibling_after_post_date = soup.find(class_="post__date").find_next_sibling().text
print(next_sibling_after_post_date.strip())

# Previous siblings
previous_sibling_post_date = soup.find(class_="post__date").find_previous_sibling().text
print(previous_sibling_post_date.strip())

# Find additional links what are at the bottom
links = soup.find(class_="additional__links").find_all("a")
print(*(f"{info.text}, {info.get('data-attr')}: {info.get('href')}" for info in links), sep="\n")

get_a_by_text = soup.find("a", string=re.compile("Clothes"))
# We can get from it what we need using text or "get"
print(get_a_by_text.text)
