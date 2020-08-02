import random   #word choice
import string   #uppercase letters in english dict 

from ThousandMostPopularWords import words  #imported list of 1000 most populr english nouns 

def get_valid_words(words):   #
    word = random.choice(words)
    while '-' in word or " " in word:
        word = random.choice(words)
    return word 

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # keeps track of all the distinct letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # keeps track of what letter user guessed 

    user_letter = input ('Guess a letter: ').upper() 
    if user_letter in alphabet - used_letters:
        used_letters.add(used_letters)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    elif user_letter is used_letters:
        print('You have already used that letter, try another one.')    
    else:
        print('You have used an invalid character.')
user_input = input('Type something:')
print(user_input)
