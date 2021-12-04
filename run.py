import random, time
marvelHeroes = ['thor', 'loki', 'vision', 'deadpool', 'hawkeye', 'mantis', 'antman']
dcHeroes = ['batman', 'superman', 'flash', 'cyborg', 'robin', 'aquaman', 'joker']
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

name = input("Enter your Gametag:")
print("Hello and Welcome", name.capitalize(), "to play Hangman game!!")
time.sleep(1)
print("You must guess the word chosen by the computer to win the game.")
time.sleep(3)
print("Each guess may be only one letter. Remember to press 'enter' after each guess.")
time.sleep(3)
print("Good luck and have fun!")
time.sleep(2)

while True:
    while True:
        if category.upper() == 'M':
            wordList = random.choice(marvelHeroes)
            break
        elif category.upper() == 'D':
            wordList = random.choice(dcHeroes)
            break
        else:
            category = input("Please choose M for Marvels, D for DC or E to exit")
        
        if category.upper() == 'E':
            print("Until next time, good luck")
            playGame = False
            break
    
    if playGame:
        secretWordList = list(wordList)
        attempts = (len(secretWord)+ 2)

        def printGuessedLetter():
            print("Your secret word is: " + ''.join(userGuesslist))
        

