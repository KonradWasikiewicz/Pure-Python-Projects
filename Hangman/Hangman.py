import random   #word choice
import string   #uppercase letters in english dict 

from ThousandMostPopularWords import words  #imported list of 1000 most popular english nouns  
from gallows import gallows 

def get_valid_word(words):   #excluding any words that might not be valid
    word = random.choice(words)
    while '-' in word or ' ' in word or '.' in word:
        word = random.choice(words)
    return word.upper()

def user_decision():     #exercised if guessing is complete
    decision = input('\nWant to play again? (Y/N)').upper()
    if decision == "Y":
        hangman()
    elif decision == "N":                
        print('Thanks for playing!')
    else:
        print('You can only agree or disagree :)')
        decision = input('\nWant to play again? (Y/N)').upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # keeps track of all the distinct letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # keeps track of what letter user have guessed (in alphabetical order)
    counter = 0  # reference to gallows drawing that appears after each bad guess
    chances = 6  # number of chances to guess the right word before the game ends 

    while len(word_letters) > 0 and chances > 0:  # len(word_letters) checks if you have already guessed it all 
        print('\nYou have', chances, 'chances and used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print(gallows[counter]) 
        user_letter = input('Guess a letter: ').upper() 
        

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)   #add used letter to the used letters set


            if user_letter in word_letters:
                word_letters.remove(user_letter)    
                print('')

            else:
                chances = chances - 1 #if wrong, decrease chances by 1 
                counter += 1
                print('\nYour letter is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter, try another one.')    
        elif len(user_letter) > 1:
            print('\nMate, give one letter please.')
        else:
            print('\nYou have used an invalid character.')
    
    if chances == 0:
        print(gallows[6])
        print('You died bro. The word was',word)
        user_decision()
    else:
        print(gallows[7])
        print('Nice job bro. You got that. The word was ',word) 
        user_decision()

if __name__ == '__main__':
    hangman()

 