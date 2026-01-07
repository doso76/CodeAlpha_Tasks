import random

words = ['book', 'pen', 'pencil', 'paper', 'chair']

secret_word = random.choice(words)
print("Welcome to hangman!")

display = []
for letter in secret_word:
    display.append('_')

print(" ".join(display))


def guess_letter():
    guess = input("Guess a letter: ").lower()
    return guess


def check_word(guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            display[i] = guess


lives = 6
while "_" in display and lives > 0:
    guess = guess_letter()
    check_word(guess)
    print(" ".join(display))

    if guess not in secret_word:
        lives -= 1
        print(f"oops, wrong guess. {lives} lives left")

if "_" not in display:
    print("congratulations ! , you won ")

else:
    print(f"Game over!. The word was {secret_word}")
