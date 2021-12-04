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
            category = input("Please choose M for Marvels, D for DC or E to exit:")
        
        if category.upper() == 'E':
            print("Until next time, good luck")
            playGame = False
            break
    
    if playGame:
        secretWordList = list(wordList)
        attempts = (len(secretWord)+ 2)

        def printGuessedLetter():
            print("Your secret word is: " + ''.join(userGuesslist))
        
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("Each guess for this word is limited to:", attempts)

        while true:

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
            if joinedList.upper() == secretWordList.upper():
                print("GoodJob!! You WON!!")
                break
            elif attempts == 0:
                printGuessedLetter("You guessed too many times!, sorry, better luck next time.")
                time.sleep(2)
                print("The secret word was: "+ secretWordList.upper())
                break