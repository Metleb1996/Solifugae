from .. constants import pEnds, wEnds, letters, inwordcharacters

def parsePhrases(text):
    phrases = set()
    charIndex = 0
    lastIndex = 0
    text = text.replace("\n", " ")
    text = text.strip()
    for i in text:
        charIndex += 1
        if i in pEnds:
            phrase = text[lastIndex:charIndex]
            lastIndex = charIndex
            phrase = phrase.strip()
            if len(phrase) > 1:
                phrases.add(phrase)
    return phrases

def parseWords(text):
    words = set()
    charIndex = 0
    lastIndex = 0
    text = text.replace("\n", " ")
    text = text.strip()
    for i in text:
        charIndex += 1
        if i in pEnds+wEnds:
            word = text[lastIndex:charIndex]
            lastIndex = charIndex
            word = word.strip()
            for j in word:
                if j not in letters+inwordcharacters:
                    word = word.replace(j, "")
            if len(word) > 1:
                words.add(word)
    return words