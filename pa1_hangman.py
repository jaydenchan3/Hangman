# assignment: programming assignment 1
# author: Jayden Chan
# date: (write the date you finished working on the program)
# file: hangman.py is a program that test_hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

from random import choice, random, randint

dictionary_file = "dictionary.txt"  # make a dictionary.txt in the same folder where hangman.py is located


# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12


def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    file = open(filename, 'r')
    dic_list = file.readlines()
    words = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    for i in dic_list:
        #x = f'{i[3:-1]}'
        x = i.strip()
        words.append(x)
    for i in words:
        if len(i) == 3:
            three.append(i)
        elif len(i) == 4:
            four.append(i)
        elif len(i) == 5:
            five.append(i)
        elif len(i) == 6:
            six.append(i)
        elif len(i) == 7:
            seven.append(i)
        elif len(i) == 8:
            eight.append(i)
        elif len(i) == 9:
            nine.append(i)
        elif len(i) == 10:
            ten.append(i)
        elif len(i) == 11:
            eleven.append(i)
        elif len(i) >= 12:
            twelve.append(i)
    for i in words:
        dictionary[3] = three
        dictionary[4] = four
        dictionary[5] = five
        dictionary[6] = six
        dictionary[7] = seven
        dictionary[8] = eight
        dictionary[9] = nine
        dictionary[10] = ten
        dictionary[11] = eleven
        dictionary[12] = twelve
    try:
        pass
    except Exception:
        pass
    return dictionary


# print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    max_size = 12
    print(import_dictionary(dictionary_file))
    pass


# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    while True:
        try:
            size = int(input('Please choose a size of a word to be guessed [3 - 12, default any size]:'))
            if 12 >= size and size >= 3:
                print(f'The word size is set to {size}.')
                break
        except ValueError:
            print('A dictionary word of any size will be chosen.')
            size = randint(3, 12)
            break
    while True:
        try:
            lives = int(input('Please choose a number of lives [1 - 10, default 5]:'))
            if lives <= 10 and lives >= 1:
                print(f'You have {lives} lives.')
                break
        except ValueError:
            print("You have 5 lives.")
            lives = 5
            break
    return size, lives


# MAIN

if __name__ == '__main__':
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    #print_dictionary(dictionary)  # remove after debugging the dictionary function import_dictionary
    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:
        # set up game options (the word size and number of lives)
        size_lives = get_game_options()
        size = size_lives[0]
        lives = size_lives[1]

        # select a word from a dictionary (according to the game options)
        # use choice() function that selects an item from a list randomly, for example:
        # mylist = ['apple', 'banana', 'orange', 'strawberry']
        # word = choice(mylist)
        myList = dictionary[size]
        word = choice(myList)
        word = word.lower()
        #print(word)
        #word = ('disappointment')
        # splits words into letters in a list
        word_split = []
        for i in word:
            word_split.append(i)

        word_upper = []
        for i in word:
            word_upper.append(i.upper())
        # print(word_split)
        # START GAME LOOP   (INNER PROGRAM LOOP)

        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        chosen_letters = []
        mistakes = 0
        live_count = lives

        # splits blank spots into a lists of letters
        blank = []
        for i in range(len(word)):
            blank.append('__')
        while lives >= 0:
            # check and adds hyphen
            if '-' in word_split:
                for i in range(len(word)):
                    if '-' == word_split[i]:
                        blank[i] = '-'

            # adds the blank spots
            print(f'Letters chosen: {", ".join(chosen_letters)}')
            blank_join = '  '.join(blank)
            print(blank_join, end='   ')
            print(f"lives: {lives} {mistakes * 'X'}{lives * 'O'}")


            # break if user has no lives, or user won
            if lives == 0: break
            if word_upper == blank: break
            # ask the user to guess a letter
            letter = input('Please choose a new letter >')

            #only allows single character letter inputs
            while not letter.isalpha() or len(letter) > 1:
                letter = input('Please choose a new letter >')

            #checks to see if letter has already been guessed
            chosen_letters_str = ''.join(chosen_letters).lower()
            while letter in chosen_letters_str or letter in chosen_letters_str:
                print('You have already chosen this letter.')
                letter = input('Please choose a new letter >')

            # update the list of chosen letters
            chosen_letters.append(letter.upper())
            # print(chosen_letters)
            chosen_letters_str = ''.join(chosen_letters).lower()
            # if the letter is correct update the hidden word,
            # else update the number of lives
            # and print interactive messages


            #if letter in chosen_letters_str or letter in chosen_letters_str:
                #print('You have already chosen this letter')

            if letter in word_split or letter.lower() in word_split:
                print('You guessed right!')
                for i in range(len(word)):
                    if letter == word_split[i] or letter.lower() == word_split[i]:
                        blank[i] = letter.upper()
            else:
                print('You guessed wrong, you lost one life.')
                lives -= 1
                mistakes += 1
                live_count -= 1
                #break

            # END GAME LOOP   (INNER PROGRAM LOOP)

            # check if the user guesses the word correctly or lost all lives,
            # if yes finish the game

        if lives <= 0:
                print(f'You lost! The word is {word.upper()}!')
        elif blank == word_upper:
                print(f'Congratulations!!! You won! The word is {word.upper()}!')
            # END MAIN LOOP (OUTER PROGRAM LOOP)

            # ask if the user wants to continue playing,
            # if yes start a new game, otherwise terminate the program

        if lives <= 0 or blank == word_upper:
            while True:
                play_again = input('Would you like to play again [Y/N]?')
                if play_again == 'y' or play_again == 'Y':
                    break
                elif play_again == 'n' or play_again == 'N':
                    print('Goodbye!')
                    quit()




