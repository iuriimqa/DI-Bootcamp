from faker import Faker
import random




print("Welcome to Hangman Game")
#to get player delails

easywords = ['sport','alphabit','nuclear']
mediumwords = ['victory','usually','nickson']
hardwords = ['status','valueble','rewards']

def input_player():
    name = input("Please type your name")
    difficulty = input("Please choose difficulty")

    if difficulty == 'easy':
        word = random.choice(easywords)
    elif difficulty == 'medium':
        word = random.choice(mediumwords)
    else:
        word = random.choice(hardwords)

    return word









# def check_letter():

# sozdai, suka, word and to_display

def get_new_letter():
    letter = input("Type new letter?")
    return letter

def make_turn(word, to_display, letter):



    return to_display

def main():
    word = input_player()
    to_display = '_' * len(word)
    letter = get_new_letter()
    while '_' not in to_display:
        if letter in word:
            letter = get_new_letter()
            to_display = make_turn(word, to_display, letter)
            print(to_display)














#
# def check_guess(word, letter, guess):
#     if letter in word:
#         printword.replace('_',letter)
#         message = print("Great!")
#
#     else:
#         guess -= 1
#
#     return guess
#
# def check_winloss(quess):
#     if '_' not in printword:
#         print("Victory")
#         Player.score += 1
#         elif quess != 0:
#             play
#         else:
#             print("Loss")
#             Player.score -= 1
#
#
# word = 'ABBA'
# lives = 3
#
#
# def play():
#     display_board
#     input_player()


# word = input_player()
# printword(word)

main()