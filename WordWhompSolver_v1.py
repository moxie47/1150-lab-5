__author__ = 'MatthewRowe'

#Open and format into a table, the dictionary
DICTIONARY = open("wordDictionary.txt", "r")
DICTIONARYstring = DICTIONARY.read()
DICTIONARYlist = DICTIONARYstring.split()

#get length of dictionary
LENGTHdictionary = len(DICTIONARYlist)

#define functions
def lengthOneWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        table = table + [string1[firstPosition]]
    return table
def lengthTwoWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        for secondPosition in range (0, LENGTHstring):
            if firstPosition != secondPosition:
                table = table + [string1[firstPosition] + string1[secondPosition]]
    return table
def lengthThreeWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        for secondPosition in range (0, LENGTHstring):
            for thirdPosition in range(0, LENGTHstring):
                if firstPosition != secondPosition and firstPosition != thirdPosition and secondPosition != thirdPosition:
                    table = table + [string1[firstPosition] + string1[secondPosition] + string1[thirdPosition]]
    return table
def lengthFourWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        for secondPosition in range (0, LENGTHstring):
            for thirdPosition in range(0, LENGTHstring):
                for fourthPosition in range(0, LENGTHstring):
                    if firstPosition != secondPosition and firstPosition != thirdPosition and secondPosition != thirdPosition\
                        and firstPosition != fourthPosition and secondPosition != fourthPosition and thirdPosition != fourthPosition:
                        table = table + [string1[firstPosition] + string1[secondPosition] + string1[thirdPosition] + string1[fourthPosition]]
    return table
def lengthFiveWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        for secondPosition in range (0, LENGTHstring):
            for thirdPosition in range(0, LENGTHstring):
                for fourthPosition in range(0, LENGTHstring):
                    for fifthPosition in range(0, LENGTHstring):
                        if firstPosition != secondPosition and firstPosition != thirdPosition and secondPosition != thirdPosition\
                            and firstPosition != fourthPosition and secondPosition != fourthPosition and thirdPosition != fourthPosition\
                            and firstPosition != fifthPosition and secondPosition != fifthPosition and thirdPosition != fifthPosition\
                            and fourthPosition != fifthPosition:
                            table = table + [string1[firstPosition] + string1[secondPosition] + string1[thirdPosition] + string1[fourthPosition] + string1[fifthPosition]]
    return table
def lengthSixWords(string1):
    LENGTHstring = len(string1)
    table = []
    for firstPosition in range(0, LENGTHstring):
        for secondPosition in range (0, LENGTHstring):
            for thirdPosition in range(0, LENGTHstring):
                for fourthPosition in range(0, LENGTHstring):
                    for fifthPosition in range(0, LENGTHstring):
                        for sixthPosition in range(0, LENGTHstring):
                            if firstPosition != secondPosition and firstPosition != thirdPosition and secondPosition != thirdPosition\
                                and firstPosition != fourthPosition and secondPosition != fourthPosition and thirdPosition != fourthPosition\
                                and firstPosition != fifthPosition and secondPosition != fifthPosition and thirdPosition != fifthPosition\
                                and fourthPosition != fifthPosition\
                                and firstPosition != sixthPosition and secondPosition != sixthPosition and thirdPosition != sixthPosition\
                                and fourthPosition != sixthPosition and fifthPosition != sixthPosition:
                                table = table + [string1[firstPosition] + string1[secondPosition] + string1[thirdPosition] + string1[fourthPosition] + string1[fifthPosition] + string1[sixthPosition]]
    return table
def checkIfInDictionary(string1):
    list = []
    if string1 in DICTIONARYlist:
        list = list + [string1]
    return list
def removeDuplicates(table1):
    LENGTHtable = len(table1)
    table = []
    for index in range(0, LENGTHtable - 1):
        if table1[index] not in table:
            table = table + [table1[index]]
    return table

def main():
    listLen3 = lengthThreeWords(userInput)
    sizelistLen3 = len(listLen3)
    listLen3.sort()
    listLen4 = lengthFourWords(userInput)
    sizelistLen4 = len(listLen4)
    listLen4.sort()
    listLen5 = lengthFiveWords(userInput)
    sizelistLen5 = len(listLen5)
    listLen5.sort()
    listLen6 = lengthSixWords(userInput)
    sizelistLen6 = len(listLen6)
    listLen6.sort()
    finalTable = []
    for index in range(0, sizelistLen3 - 1):
        finalTable = finalTable + checkIfInDictionary(listLen3[index])
    for index in range(0, sizelistLen4 - 1):
        finalTable = finalTable + checkIfInDictionary(listLen4[index])
    for index in range(0, sizelistLen5 - 1):
        finalTable = finalTable + checkIfInDictionary(listLen5[index])
    for index in range(0, sizelistLen6 - 1):
        finalTable = finalTable + checkIfInDictionary(listLen6[index])
    finalTable = removeDuplicates(finalTable)
    print(finalTable)
    print("The number of words is:", len(finalTable))


#get user input
userInput = input("What letters are given? [type all the letters as one word]: ")

#call main
main()