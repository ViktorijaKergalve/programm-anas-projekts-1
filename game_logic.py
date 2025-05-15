class WordGame:
    def __init__(self, secret_word):
        self.secret_word = secret_word:
        self.guessed_letters = []
        self.tries_left = 6

    def display_word(self):
        display =  ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += " _ "
        return display.strip()
