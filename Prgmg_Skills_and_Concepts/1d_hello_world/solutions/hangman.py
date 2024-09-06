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
               
def play_game(word_length, word_list):
    list_of_x_letter_words = [
        word for word in word_list if len(word) == word_length
    ]
    
    random_word = random.choice(list_of_x_letter_words)

    hm_progress = 0
    guessed_characters = 0
    guessed_letters = []

    current_state = ["_" for x in range(word_length)]

    for char in current_state:
        print(f"{char} ", end='')
    print()

    print_hangman_image(hm_progress)

    while hm_progress < 7:
        selected_letter = input("Please input a letter : ")

        if selected_letter in guessed_letters:
            print (f"You've guessed {selected_letter} before, try another.")
        else:
            guessed_letters.append(selected_letter)
            if selected_letter in random_word:
                print (f"Correct!  {selected_letter} is in the word!")
                for char_index in range(word_length):
                    if random_word[char_index] == selected_letter:
                        current_state[char_index] = selected_letter
                        guessed_characters += 1
            else:
                print (f"Sorry, there's no {selected_letter}")
                hm_progress += 1

        if guessed_characters == word_length:
            print ("Well done - you win!")
            break
        
        for char in current_state:
            print(f"{char} ", end='')
        print()

        print_hangman_image(hm_progress)

        time.sleep(1)
        
    print (f"The word was {random_word}")
        
length_of_word = int(input("Please input number of letters for word : "))
play_game(length_of_word, list_of_words)

