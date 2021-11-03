import os
import requests
from bs4 import BeautifulSoup

def walker(url, header):
    page = requests.get(url, headers=header)
    page = BeautifulSoup(page.content, "html5lib") #lxml, html5, html5lib
    links_div = page.find("div", attrs={"id":"recent-posts-2"})
    links_ = links_div.find("ul").find_all("li")
    links = []
    for li in links_:
        a = li.find("a")
        links.append(a["href"])
    return links

def parser(url:str, header):
    page = requests.get(url, headers=header)
    page = BeautifulSoup(page.content, "html5lib") #lxml, html5, html5lib
    article_text = page.find_all("div", attrs={"class":"entry-content"})
    slug = url.rsplit('/')[-2]
    return article_text[0].text, slug

def writer(text, name):
    if not os.path.exists(name):
        with open(name, "w") as f:
            f.write(text)
        return True
    return False