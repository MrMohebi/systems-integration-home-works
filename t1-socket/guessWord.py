import random


def get_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'peach', 'kiwi']
    return random.choice(words)
class WordGuess:
    target_word: str
    guessed_word: str
    attempts:int
    is_finish:bool
    def __init__(self):
        self.target_word = get_random_word()
        self.guessed_word = '_' * len(self.target_word)
        self.attempts = 6
        self.is_finish = False

    def show_current_state(self):
        returnVal = ""
        if self.attempts > 0:
            returnVal += ' '.join(self.guessed_word) + "\n"
            returnVal += f"Attempts left: {self.attempts}" + "\n"
        else:
            returnVal += f"Game over! The word was: {self.target_word}"
            self.is_finish = True
        return returnVal
    def play_game(self, userInp):
        returnVal = ""
        while self.attempts > 0 and not self.is_finish:
            guess = userInp.lower()

            if len(guess) == 1:
                if guess in self.target_word:
                    for i in range(len(self.target_word)):
                        if self.target_word[i] == guess:
                            self.guessed_word = self.guessed_word[:i] + guess + self.guessed_word[i+1:]
                    if '_' not in self.guessed_word:
                        returnVal += f"Congratulations! You guessed the word: {self.target_word}" + "\n"
                        self.is_finish = True
                        return returnVal
                else:
                    returnVal +=  "Incorrect guess!" + "\n"
                    self.attempts -= 1
            elif len(guess) == len(self.target_word):
                if guess == self.target_word:
                    returnVal += f"Congratulations! You guessed the word: {self.target_word}" + " \n"
                    self.is_finish = True
                    return returnVal
                else:
                    returnVal += "Incorrect guess!" + "\n"
                    self.attempts -= 1
            else:
                returnVal += "Invalid guess! Please enter a single letter or the whole word." + "\n"

            return returnVal

