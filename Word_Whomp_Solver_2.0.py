__author__ = 'MatthewRowe'

from itertools import *

#Open and format into a table, the dictionary
DICTIONARY = open("wordDictionary.txt", "r")
DICTIONARYstring = DICTIONARY.read()
DICTIONARYlist = DICTIONARYstring.split()

#get length of dictionary
LENGTHdictionary = len(DICTIONARYlist)

#define functions
def LengthRwords(string1, R):
    """Returns a table of all the permutations of length R for string1"""

    table = [''.join(i) for i in permutations(string1, R)]
    return table

def checkIfInDictionary(string1):
    """checks if string1 is in the English Language Dictionary and
    returns it as an item in a list"""

    list = []
    if string1 in DICTIONARYlist:
        list = list + [string1]
    return list

def removeDuplicates(list1):
    """Removes any duplicate entries for a list
    [Needed if double letters exist (because Permutation isn't aware of those)]"""

    LENGTHtable = len(list1)
    table = []
    for index in range(0, LENGTHtable - 1):
        if list1[index] not in table:
            table = table + [list1[index]]
    return table

def main():
    """Returns all solutions for Word-Whomp Game via Pogo.com
    for a User-Entered set of six letters."""

    #create four lists each filled with all possible combinations of R letter words from the userInput
    listLen3 = LengthRwords(userInput, 3)
    listLen4 = LengthRwords(userInput, 4)
    listLen5 = LengthRwords(userInput, 5)
    listLen6 = LengthRwords(userInput, 6)

    #sorts each list alphabetically
    listLen3.sort()
    listLen4.sort()
    listLen5.sort()
    listLen6.sort()

    #concatenates lists into one large list
    allWords = []
    allWords = allWords + listLen3 + listLen4 + listLen5 + listLen6

    #checks if each word is in the Dictionary, and returns it if it is
    sizeAllWords = len(allWords)
    finalList = []
    for index in range(0, sizeAllWords - 1):
        finalList = finalList + checkIfInDictionary(allWords[index])

    #removes duplicates from the list
    finalList = removeDuplicates(finalList)

    #prints the list one word per line
    for word in finalList:
        print(word)

    #prints the total number of words in the list
    print("The number of words is:", len(finalList))

#get user input
userInput = input("What letters are given? [type all the letters as one word]: ")

#call main
main()

#close file
DICTIONARY.close()
