import random

def get_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'peach', 'kiwi']
    return random.choice(words)

def play_game():
    target_word = get_random_word()
    guessed_word = '_' * len(target_word)
    attempts = 6

    while attempts > 0:
        print(' '.join(guessed_word))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in target_word:
                for i in range(len(target_word)):
                    if target_word[i] == guess:
                        guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
                if '_' not in guessed_word:
                    print(f"Congratulations! You guessed the word: {target_word}")
                    return
            else:
                print("Incorrect guess!")
                attempts -= 1
        elif len(guess) == len(target_word):
            if guess == target_word:
                print(f"Congratulations! You guessed the word: {target_word}")
                return
            else:
                print("Incorrect guess!")
                attempts -= 1
        else:
            print("Invalid guess! Please enter a single letter or the whole word.")

    print(f"Game over! The word was: {target_word}")

