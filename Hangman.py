import random

def choose_word():
    words = ['python', 'java', 'hangman', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1

        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: '{word}'")
            break
    else:
        print(f"\nGame over! The word was: '{word}'")

if __name__ == "__main__":
    hangman()
