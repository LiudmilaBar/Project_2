"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Liudmila Baravets
email: liudmila.baravets@gmail.com
"""
import random

import time

cara = "-" * 50

def generate_secret_number() -> str:
    """
    Vygeneruje čtyřciferné tajné číslo složené z různých číslic, nezačínající nulou.
    """
    digits = list("0123456789")
    while True:
        number = ''.join(random.sample(digits, 4))
        if number[0] != "0":
            return number


def is_valid(guess: str) -> bool:
    """
    Ověří, zda je vstup správně zadané čtyřciferné číslo s různými číslicemi.
    """
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


def count_bulls_and_cows(secret: str, guess: str) -> tuple[int, int]:
    """
    Spočítá počet bulls (správná číslice na správném místě)
    a cows (správná číslice na špatném místě).
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def plural(count: int, word: str) -> str:
    """
    Vrátí správné jednotné/množné číslo pro výpis.
    """
    if count == 1:
        return f"{count} {word}"
    else:
        return f"{count} {word + 's'}"


def play_game() -> None:
    """
    Spustí hru Bulls and Cows a zajišťuje hlavní smyčku hry.
    """
    print("Hi there!")
    print(cara)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(cara)

    secret = generate_secret_number()
    attempts = 0
    start = time.time()

    while True:
        try:
            guess = input("Enter a number: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Goodbye!")
            return

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
if __name__ == "__main__":
    play_game()