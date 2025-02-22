import random
from words import words

import string

def get_valid_word(words):
    word = random.choices(word) # randomly chooses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters =set() # what the user has guessed 
    
    lives =7
    
    #getting user input 
    while len(word_letters) > 0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        #what current word is (ie w-R D)
        word_list =[letter if letter in used_letters else '-' for letter in word]
        
        print('current word: ',  ' '.join(word_list))
        
        
        user_letter =input ('Guess a letter: ').upper()
        if user_letter in alphabet- used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
                
                
        elif user_letter in used_letters:
            print('You have already used that charcter. Please try again.')
        else:
            print('Invalid character. Please try again.')
    
    
    
user_input = input ('Type something : ')
print(user_input)