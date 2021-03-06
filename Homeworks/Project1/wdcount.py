import sys
import os

def find_file(file_name):
    """
    finds and extracts the raw data from the teext file file_name
    Returns: A list of all words
    """
    data = list()
    with open(file_name) as file:
        for row in file:
            data += row.split(' ')

    for i, word  in enumerate(data): #removes the new line character
        if '\n' in word:
            data[i] = word.strip('\n')

    #print(data)
    return data

def create_dict(data):
    datadict = dict()
    for word in data:
        if word.lower() not in datadict:
            datadict[word.lower()] = 1
        else:
            datadict[word.lower()] += 1
            
    return datadict

def main():
    """
    Author: Peter Parianos

    This program will count the number of words in a file given as a command line argument,
    store each name and the number of occurences in a dict,
    then print words based on certain conditions:
        Number of different words (number of dictionary entries)
        Total number of words in the file (num of dict entries * number of occurences)
        Each word that has more than 4 characters along with its number of occurrences (most frequent word should be printed first)
            - key length greater than 4
        The longest word in the file (either one if there is two of the same length)
            - maximum key length

    DUE: Sept. 13th - CIS424s
    turnin -c cis424s -p proj1 wdcount.py
    """
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('No argument found, exiting...')
        exit()

    data = find_file(file_name)
    datadict = create_dict(data)

    print("Number of unique words: ", len(datadict))
    print("Total number of words: ", len(data))

    #The longest word in the file
    #sortedList = sorted(data, key= lambda word: len(word), reverse=True)
    #print("longest word in the file: ", sortedList[0])

    maxword = data[0]
    for word in data:
        if len(word) >= len(maxword):
            maxword = word
    print("longest word in the file: ", maxword)

    

    #Each word that has more than 4 characters along with its number of ocurrences
    print("These words have more than 4 characters:")
    temp_list = list()
    for key in datadict.keys():
        if len(key) > 4:
            temp_list.append(key)
    temp_list = sorted(temp_list, key = datadict.get, reverse=True)
    for word in temp_list:
        print("word: %s, Number of Occurrences: %s" % (word, datadict.get(word)))


main()
