import random   #word choice
import string   #uppercase letters in english dict 

from ThousandMostPopularWords import words  #imported list of 1000 most populr english nouns  


def get_valid_word(words):   #excluding any words that might not be valid
    word = random.choice(words)
    while '-' in word or ' ' in word or '.' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # keeps track of all the distinct letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # keeps track of what letter user have guessed (in alphabetical order)
    chances = 5 

    #user input
    while chances > 0:
        print('You have', chances, 'chances and used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)   #add used letter to the used letters set
            if user_letter in word_letters:
                word_letters.remove(user_letter)    
                print('')
            else:
                chances = chances - 1 #if wrong, decrease chances by 1 
                print('\nYour letter is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter, try another one.')    
        elif len(user_letter) > 1:
            print('Mate, give one latter plese.')
        else:
            print('\nYou have used an invalid character.')
    
    if chances == 0:
        print('\nYou died bro. The word was', word)
    else:
        print('\nNice job bro. You got that.') 

if __name__ == '__main__':
    hangman()


#https://github.com/kying18/hangman/blob/master/hangman.py
