import os
import sys
from core.collector import adpu_q_get_all_links
from core.parser import parsePhrases, parseWords, parseSyllables
from core.constants import header, ARTICLES_DIR
from core.globalfunctions import lover

phrases = set()
words = set()
syllables = set()

def merge():
    with open(os.getcwd()+ARTICLES_DIR+"merged.txt", "w") as merged_f:
        for file in os.listdir(os.getcwd()+ARTICLES_DIR):
            with open(os.getcwd()+ARTICLES_DIR+file, "r") as _f:
                text = _f.read()
            merged_f.write(text)

def main(step, url, parse):
    text = ''
    if step == "collect":
        adpu_q_get_all_links(url=url, header=header, limit=1)
    elif step == "merge":
        merge()
    elif step == "parse":
        with open(os.getcwd()+ARTICLES_DIR+"merged.txt", "r") as text_f:
            text = text_f.read()
        if parse == "phrases":
            phrases.update(parsePhrases(text))
        elif parse == "words":
            words.update(parseWords(text)) 
        elif parse == "syllables":
            words.update(parseWords(text))
            for w in words:
                syllables.update([lover(x) for x in parseSyllables(w)]) 
    else:
        return False


if __name__ == '__main__':
    step = "collect"
    url = "https://adpuquba.edu.az/ilham-heyd%c9%99r-oglu-%c9%99liyevin-ilk-d%c9%99f%c9%99-prezident-secilm%c9%99sind%c9%99n-18-il-otur/"
    parse = "phrases"
    if len(sys.argv)>1:
        for arg in sys.argv:
            if arg == "--step":
                step = sys.argv[sys.argv.index(arg)+1]
            if arg == "--url":
                url = sys.argv[sys.argv.index(arg)+1]
            if arg == "--parse":
                parse = sys.argv[sys.argv.index(arg)+1]
    main(step, url, parse)
    # if parse == "phrases":
    #     for p in phrases:
    #         print(p)
    # elif parse == "words":
    #     for w in words:
    #         print(w)
    # elif parse == "syllables":
    #     for s in syllables:
    #         print(s)
    print(len(phrases), len(words), len(syllables))
        
