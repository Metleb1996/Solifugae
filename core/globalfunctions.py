from .constants import letters

def lover(text):
    lText = ''
    for i in text:
        if i in letters:
            if letters.index(i) % 2 == 0:
                i = letters[letters.index(i)+1]
        lText += i
    return lText

def upper(text):
    uText = ''
    for i in text:
        if i in letters:
            if letters.index(i) % 2 == 1:
                i = letters[letters.index(i)-1]
        uText += i
    return uText
