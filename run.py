import random, time
"""import random for random choice and 
time for some time delays between the text"""

marvelHeroes = ['thor', 'loki', 'vision', 'deadpool', 'hawkeye', 'mantis', 'antman']
dcHeroes = ['batman', 'superman', 'flash', 'cyborg', 'robin', 'aquaman', 'joker']
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
print("Each guess may be only one letter. Remember to press 'enter' after each guess.")
time.sleep(2)
print("Good luck and have fun!")
time.sleep(1)
"""Game info, rules and put some paus in between the text so easier to read,
and where you can enter your name"""

while True:
    while True:
        if category.upper() == 'M':
            wordList = random.choice(marvelHeroes)
            break
        elif category.upper() == 'D':
            wordList = random.choice(dcHeroes)
            break
        else:
            category = input("Please choose M for Marvels, D for DC or E to exit:")
        
        if category.upper() == 'E':
            print("Until next time, good luck")
            playGame = False
            break
""" This is were random rules come in when you describe which category you have choose
then the computer take a random from the list either dcheroes or marvelheroes,
it depends which one you choose"""    
    
    if playGame:
        secretWordList = list(wordList)
        attempts = (len(wordList)+ 2)

        def printGuessedLetter():
            print("Your word is: " + ''.join(userGuesslist))
        
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("Each guess for this word is limited to:", attempts)
""" here is for how many attempts you have and when the game
end show what words you have atlast"""

        while True:

            print("guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("This letter is already guessed, try something else..")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Your guess is correct!")
                    if attempts > 0:
                        print("You have", attempts, 'left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()
                
                else:
                    print("Sorry! Try again")
                    if attempts > 0:
                        print("You have", attempts, 'left!')
                    printGuessedLetter()

            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == wordList.upper():
                print("GoodJob!! You WON!!")
                break
            elif attempts == 0:
                print("You guessed too many times!, sorry, better luck next time.")
                time.sleep(1)
                print("The secret word was: "+ wordList.upper())
                break

        continueGame = input("To play again, press Y, any other key to quit:")
        if continueGame.upper() == 'Y':
            category = input("Please choose M for Marvels, D for DC:")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("I thank you for playing and hope to see you next time!")
            break
    else:
        break