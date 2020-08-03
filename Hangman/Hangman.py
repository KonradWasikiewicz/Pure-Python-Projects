import random   #word choice
import string   #uppercase letters in english dict 

from ThousandMostPopularWords import words  #imported list of 1000 most populr english nouns 

def get_valid_words(words):   #excluding any words that might be 
    word = random.choice(words)
    while '-' in word or ' ' in word or '.' in word:
        word = random.choice(words)
    return word 

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # keeps track of all the distinct letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = sorted(set()) # keeps track of what letter user have guessed (in alphabetical order)
    chances = 5 

    #user input
    while chances > 1:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]

        print('Current word: ', ' '.join(word_list))

        user_letter = input ('Guess a letter: ').upper() 
        if user_letter in alphabet - used_letters:
            used_letters.add(used_letters)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter is used_letters:
            print('You have already used that letter, try another one.')    
        else:
            print('You have used an invalid character.')

if __name__ == '__main__':
    hangman()