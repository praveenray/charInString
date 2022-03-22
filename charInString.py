import string


def findposition():
    location = sentence.find(letter)
    print('The letter "' + letter + '" is found at ' + str(location))

sentence = input("Write the sentence: ")
letter = input("Write the letter: ")

findposition()
