import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in words:
        word = random.choice(words)
    return word

def hangman():
        word = get_valid_word(words)
        word_letters = set(word) #letters in a selected word
        alphabet = set(string.ascii_uppercase) #used for the user not to choose something else
        used_letters = set() #what user guessed

        #getting user input
        while len(word_letters) > 0:
            #letters user used
            #join changes the list into a string separated by whatever the string 
            #what current words is
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word: ', ' '.join(word_list))
            print('You have already used letters: ', ' ' .join(used_letters))
            user_letter = input('Guess a letter').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)

            elif user_letter in used_letters:
                print('You have already used that letter')
            
            else:
                print('Invalid letter')

hangman()
