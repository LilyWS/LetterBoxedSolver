import nltk
from nltk.corpus import words

#nltk.download("words")

#sideInput = input("Please enter sides, 3 letters followed by | for each side")

sides = [
    ["e", "o", "s"],
    ["a", "r", "u"],
    ["i", "h", "l"],
    ["z", "m", "b"]
]

word_list = set(word.lower() for word in words.words())
validWords = set()

def getSide(letter):
    for side in sides:
        if letter in side:
            return(side)
    return False

for side in sides:
    for letter in side:
        for word in word_list:
            if word[0] == letter:
                print(type(word))
                print(word)
                getSide(word[0])

def getValidWords(letter, maxLength):
    currentSide = getSide(letter)
    currentWords = set()
    for word in word_list:
        if word[0] == letter:
            
            getSide(word[0])
