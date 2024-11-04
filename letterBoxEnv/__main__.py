import nltk
from nltk.corpus import words

#nltk.download("words")

#sideInput = input("Please enter sides, 3 letters followed by | for each side")

sides = [
    ["e", "r", "a"],
    ["i", "p", "f"],
    ["t", "n", "c"],
    ["x", "o", "m"]
]

wordList = set(word.lower() for word in words.words())
validWords = set()

def getSide(letter):
    for side in sides:
        if letter in side:
            return(side)
    return False

#for side in sides:
#    for letter in side:
#        for word in word_list:
#            if word[0] == letter:
#                print(type(word))
#                print(word)
#                getSide(word[0])

def generate_words(current_word, current_side, max_length=8):
    if len(current_word) == 1:
        print(current_word)
    if len(current_word) > max_length:
        return  

    # Base case: if we formed a valid word, add it to the result
    if len(current_word) > 2 and current_word.lower() in wordList:
        validWords.add(current_word.lower())
    
    # Try adding each letter from a different side than the current one
    for side in sides:
        if side != current_side:  
            for letter in side:
                generate_words(current_word + letter, side)
    
for side in sides:
    for letter in side:
        generate_words(letter, side)


print(validWords)