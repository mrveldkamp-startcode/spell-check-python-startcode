# Spell Check Starter

import re


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    print(dictionary[0:50])
    print(aliceWordsFull[0:50])

# end main()


def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w]+", textData)


# Call main() to begin program
main()
