import os
from core.collector import walker, parser, writer
from core.constants import header


all_links = []
i = 0

def get_all_links(url, header, a):
    a+=1
    if a > 4:
        return
    links = walker(url, header=header)
    for link in links:
        if not link in all_links:
            all_links.append(link)
            text, name = parser(link, header)
            name = os.path.join(os.getcwd(), "articles/"+name+".txt")
            if writer(text, name):
                print(a, " ))  ", link, "          Added&Created  all:", len(all_links))
        print(a, " ))  ", link)
    for link in links:
            get_all_links(link, header, a=a)
    a-=1


if __name__ == '__main__':
    get_all_links("https://adpuquba.edu.az/ilham-heyd%c9%99r-oglu-%c9%99liyevin-ilk-d%c9%99f%c9%99-prezident-secilm%c9%99sind%c9%99n-18-il-otur/", header=header, a=i)

        
