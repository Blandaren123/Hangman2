import random, time
marvelHeroes = ['thor', 'loki', 'vision', 'deadpool', 'hawkeye', 'mantis', 'antman']
dcHeroes = ['batman', 'superman', 'flash', 'cyborg', 'robin', 'aquaman', 'joker']
playGame = True
category = ""
continueGame = "Y"

name = input("Enter your Gametag:")
print("Hello and Welcome", name.capitalize(), "to play Hangman game!!")
time.sleep(1)
print("You must guess the secret word chosen by the computer to win the game.")
time.sleep(3)
print("Each guess may be only one letter. Remember to press 'enter' after each guess.")

