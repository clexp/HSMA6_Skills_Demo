# need to pip install nltk

import nltk
nltk.download('words')

from nltk.corpus import words
import random
import time

list_of_words = words.words()

#print (random_word)

print ()

def print_hangman_image(progress):
    if progress == 0:
        print ()
    elif progress == 1:
        print ("|       ")
        print ("|       ")
        print ("|       ")
        print ("|       ")
        print ("|       ")
    elif progress == 2:
        print ("|=====  ")
        print ("|       ")
        print ("|       ")
        print ("|       ")
        print ("|       ")
    elif progress == 3:
        print ("|=====  ")
        print ("|    |  ")
        print ("|       ")
        print ("|       ")
        print ("|       ")
    elif progress == 4:
        print ("|=====  ")
        print ("|    |  ")
        print ("|    0  ")
        print ("|       ")
        print ("|       ")
    elif progress == 5:
        print ("|=====  ")
        print ("|    |  ")
        print ("|    0  ")
        print ("|    |  ")
        print ("|       ")
    elif progress == 6:
        print ("|=====  ")
        print ("|    |  ")
        print ("|    0  ")
        print ("|   /|\ ")
        print ("|       ")
    elif progress == 7:
        print ("|=====  ")
        print ("|    |  ")
        print ("|    0  ")
        print ("|   /|\ ")
        print ("|   / \ ")
               
