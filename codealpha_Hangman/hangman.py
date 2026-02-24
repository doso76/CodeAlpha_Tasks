import random


def choose_word():
    words = ['book', 'pen', 'pencil', 'paper', 'chair']
    return random.choice(words)


def initialize_display(word):
    return ['_' for _ in word]


def guess_letter():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single valid letter.")


def update_display(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess


def main():
    print("Welcome to Hangman!")

    secret_word = choose_word()
    display = initialize_display(secret_word)
    lives = 6
    guessed_letters = []

    print(" ".join(display))

    while "_" in display and lives > 0:
        guess = guess_letter()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            update_display(secret_word, display, guess)
            print("Correct guess!")
        else:
            lives -= 1
            print(f"Wrong guess. {lives} lives remaining.")

        print(" ".join(display))

    if "_" not in display:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was '{secret_word}'.")


if __name__ == "__main__":
    main()
