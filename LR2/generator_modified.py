"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

def getWords(filename):
     # single new function named getWords
    vocab_File = open(filename) 
        #open .txt file 
    temporary_List = list()
        #creation of a new list
    for each_Line in vocab_File:
        each_Line = each_Line.strip()
        temporary_List.append(each_Line)

    words = tuple(temporary_List)
    # conversion of list to tuple

    vocab_File.close #close .txt file

    return words

#vocabulary is stored 
articles = getWords('articles.txt')

nouns = getWords('nouns.txt')

verbs = getWords('verbs.txt')

prepositions = getWords('prepositions.txt')

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

