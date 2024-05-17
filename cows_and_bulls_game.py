import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
number = []
guess = ''
tries = 0

random.shuffle(numbers)


def random_number(number):
    number += numbers.pop(0)


def cows_bulls():
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    print(f'Bulls: {bulls}, cows {cows}')


def main():
    global guess, tries
    print('Welcome to Cows&Bulls game!')
    while guess != number:
        guess = str(input('Enter 4 digit number: '))
        if len(guess) != 4:
            print('4 digits please! ')
        else:
            cows_bulls()
            tries += 1
    print(f'You are correct! number was {number}! You guessed it after {tries} tries!')


for _ in range(4):
    random_number(number)
number = "".join(dict.fromkeys(number))

main()
