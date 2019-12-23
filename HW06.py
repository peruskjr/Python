def twoWords(length, firstLetter):
    while True:
        word1 = input("Please enter a " + str(length) + "letter word: ")

        if len(word1) == length:
            break
    while True:
        word2 = input("Please enter a word that starts with " + firstLetter + " please: ")

        if word2[0].lower() == firstLetter.lower():
            break

    return [word1, word2]

print(twoWords(4, 'b'))
