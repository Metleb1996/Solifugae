from .. constants import pEnds, wEnds, letters, inwordcharacters

def parsePhrases(text):
    phrases = set()
    lastIndex = 0
    text = text.replace("\n", " ")
    text = text.strip()
    for charIndex, i in enumerate(text):
        if i in pEnds:
            phrase = text[lastIndex:charIndex+1]
            lastIndex = charIndex+1
            phrase = phrase.strip()
            if len(phrase) > 1:
                phrases.add(phrase)
    return phrases

def parseWords(text, charset=letters):
    words = set()
    lastIndex = 0
    text = text.replace("\n", " ")
    text = text.strip()
    for charIndex, i in enumerate(text):
        if i in pEnds+wEnds:
            word = text[lastIndex:charIndex]
            lastIndex = charIndex
            word = word.strip()
            for j in word:
                if j not in charset:
                    word = word.replace(j, "")
            if len(word) > 1:
                words.add(word)
    return words

def parseSyllables(text):
    syllables = list()
    text = text.replace("\n", " ")
    text = text.strip()
    syllab = ''
    sc = 0
    textmap = ''
    for i in text: #create textMap
        if i in letters:
            if i in letters[0:18]:
                textmap += 'v'
            else:
                textmap += 'c'
        else:
            raise ValueError("{} not a valid letter in {}".format(i, text))
    textmap = textmap.replace('cv', '-cv')
    textmap = textmap.replace('vv', 'v-v')
    textmap = textmap.strip('-')
    for index, i in enumerate(textmap):
        if i != '-':
            syllab = syllab + text[index-sc]
        else:
            syllables.append(syllab)
            syllab = ''
            sc += 1
        if index == len(textmap) -1:
            syllables.append(syllab)
    return syllables