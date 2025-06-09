"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Liudmila Baravets
email: liudmila.baravets@gmail.com
"""
import random

import time

cara = "-" * 50
# tajné číslo (4 různé číslice, nezačíná nulou)
def generate_secret_number():
    digits = list("0123456789")
    while True:
        number = " ".join(random.sample(digits, 4))
        if number[0] != "0":
            return number

#  platnost vstupu
def is_valid(guess):
    if not guess.isdigit():
        print("Input must be a number.")
        return False
    if len(guess) != 4:
        print("The number must have 4 digits.")
        return False
    if guess[0] == "0":
        print("The number must not start with a zero.")
        return False
    if len(set(guess)) != 4:
        print("Digits must not be repeated.")
        return False
    return True

# Spočítá bulls a cows
def count_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# Pomůže s jednotným/množným číslem
def plural(count, word):
    if count == 1:
        return f"{count} {word}"
    else:
        return f"{count} {word + 's'}"

# Hra samotná
def play_game():
    print("Hi there!")
    print(cara)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(cara)

    secret = generate_secret_number()
    attempts = 0
    start = time.time()

    while True:
        guess = input("Enter a number:").strip()
        if not is_valid(guess):
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)

        if bulls == 4:
            duration = round(time.time() - start, 2)
            print(f"Correct, you've guessed the right number {secret} in {attempts} guesses!")
            print(cara)
            print("That's amazing!")
            print(f"Time: {duration} s.")
            break
        else:
            print(f"{plural(bulls, 'bull')}, {plural(cows, 'cow')}")
            print(cara)
            print("Try again!")
play_game()