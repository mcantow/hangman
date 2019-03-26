# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:06:04 2019

@author: MCantow
"""



#game of hangman, users lose on sixth incorrect guess


import random
import string

possible_phrases = ['paul is dirty']
phrase = random.choice(possible_phrases)



class display_letters(object):
    def __init__(self, phrase, guesses):
        '''
        arguments:
        phrase: string of desired phrase
        guesses: list of strings of guessed letters
        '''
        self.phrase = phrase
        self.guesses = guesses
        self.incorrect_guesses = []
        for i in guesses:
            if str(i) not in phrase:
                self.incorrect_guesses.append(i)       
        self.s = ''
        
    def display(self):
        for i in self.phrase:
            if i in self.guesses:
                self.s += ' ' + i + ' '
            elif i in string.ascii_lowercase:
                self.s += ' _ '
            else:
                self.s += '  ' 
        print(self.s)
        print(self.guesses)

        x = len(self.incorrect_guesses)
        if x == 0:
            print('6 incorrect attempts remianing')
        if x == 1:
            print('|  5 incorrect attempts remianing')
        if x == 2:
            print('|-O  4 incorrect attempts remianing')
        if x == 3:
            print('|-O>   3 incorrect attempts remianing')
        if x == 4:
            print('|-O>-   2 incorrect attempts remianing')
        if x == 5:
            print('|-O>-<  Last Guess!')
        if x == 6:
            print('|-O>-<     uh oh')
            
    def isvalidguess (self, guess):
        if guess in self.phrase:
            return True
        return False
            
    def check_game_loss(self):
        if len(self.incorrect_guesses) > 5:
            return True
        return False
    def check_game_won(self):
        for i in self.phrase:
            if i == ' ':
                pass
            elif i not in self.guesses:
                return False
        return True
        
        
def run_hangman(phrase):     
    print('Welcome to hangman, guess my word in under six incorrect guesses to win!')
    print('If you want to guess the phrase, type it in!')
    guesses = [] #list of strings representing guesses
    game = display_letters(phrase, guesses)
    game.display()
    correct_phrase = False
    
    
    while not game.check_game_loss():
        g = input('Please guess a letter or type the phrase...')
        g = g.lower()
        if len(g) > 1:
            if (g == phrase):
                correct_phrase = True
                break
            else:
                print("Sorry, that's not it")
                guesses.append(g)
                game = display_letters(phrase, guesses)
                game.display()
        else:
            guesses.append(g)
            game = display_letters(phrase, guesses)
            if game.isvalidguess(g):
                print('Correct!')
                
            else:
                print("Sorry, that's not it")
            game.display()
            if game.check_game_won():
                break
            

            
    if game.check_game_won() or correct_phrase:
        print('Congrats! You Win!!!!')
    else:
        print("Sorry, you lost. Thanks for playing! Here's the phrase:")
        print(phrase)
                
                
            
                
        
#
run_hangman(phrase)

            
            

    

            
        

            
