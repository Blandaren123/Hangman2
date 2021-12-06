import random
import time
"""import random for random choice and
time for some time delays between the text"""

marvelHeroes = ['thor', 'loki', 'vision', 'hawkeye', 'mantis', 'antman']
dcHeroes = ['batman', 'superman', 'cyborg', 'robin', 'aquaman', 'joker']
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"
"""Created container list for the random word in 2 different category and
define som var that i used in the game"""

name = input("Enter your Gametag:")
print("Hello and Welcome", name.capitalize(), "to play Hangman game!!")
time.sleep(1)
print("You must guess the word chosen by the computer to win the game.")
time.sleep(2)
print("Each guess may be only one letter. Press 'enter' after each guess.")
time.sleep(2)
print("Good luck and have fun!")
time.sleep(1)
"""Game info, rules and put some paus in between the text so easier to read,
and where you can enter your name"""

while True:

    while True:   # random generator from differentlist 2 different list
        if category.upper() == 'M':
            secretWord = random.choice(marvelHeroes)
            break
        elif category.upper() == 'D':
            secretWord = random.choice(dcHeroes)
            break
        else:
            category = input("Choose M for Marvel / D for DC or X to exit:")

        if category.upper() == 'X':
            print("Until next time, good luck")
            playGame = False  # if you choose X the game gets false and stop
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)

        def printGuessedLetter():  # this print your guess letter
            print("Your word is: " + ''.join(userGuesslist))
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("Each guess for this word is limited to:", attempts)
        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You have guessed this letter, try another.")

            else:  # show how much attempt you have left
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Your guess is Correct!")
                    if attempts > 0:
                        print("You have ", attempts, 'left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:  # when you choose wrong letter and attempt left
                    print("Sorry! Try again.")
                    if attempts > 0:
                        print("You have", attempts, 'left!')
                    printGuessedLetter()
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("GoodJob!! You WON!!")
                break
            elif attempts == 0:  # no attempt left it tells you that
                print("You guessed too many times!, better luck next time.")
                print("The secret word was: " + secretWord.upper())
                break
        continueGame = input("To play again, press Y, any other key to quit:")
        if continueGame.upper() == 'Y':
            category = input("Please choose M for Marvels, D for DC:")
            userGuesslist = []
            userGuesses = []
            playGame = True  # if press y the game will restart play again
        else:
            print("I thank you for playing and hope to see you next time!")
            break
    else:
        break
    