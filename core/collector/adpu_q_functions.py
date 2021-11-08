import os
import requests
from bs4 import BeautifulSoup
from .writer import writer

all_links = []

def adpu_q_walker(url, header):
    page = requests.get(url, headers=header)
    page = BeautifulSoup(page.content, "html5lib") #lxml, html5, html5lib
    links_div = page.find("div", attrs={"id":"recent-posts-2"})
    links_ = links_div.find("ul").find_all("li")
    links = []
    for li in links_:
        a = li.find("a")
        links.append(a["href"])
    return links

def adpu_q_parser(url:str, header):
    page = requests.get(url, headers=header)
    page = BeautifulSoup(page.content, "html5lib") #lxml, html5, html5lib
    article_text = page.find_all("div", attrs={"class":"entry-content"})
    slug = url.rsplit('/')[-2]
    return article_text[0].text, slug


def adpu_q_get_all_links(url, header, limit, a = 0):
    a+=1
    if a > limit:
        return
    links = adpu_q_walker(url, header=header)
    for link in links:
        if not link in all_links:
            all_links.append(link)
            text, name = adpu_q_parser(link, header)
            name = os.path.join(os.getcwd(), "articles/"+name+".txt")
            if writer(text, name):
                print( a, " ))  ", link, "          Added&Created  all:", len(all_links))
        print(a, " ))  ", link)
    for link in links:
            adpu_q_get_all_links(link, header, limit=limit, a=a)
    a-=1
    return True