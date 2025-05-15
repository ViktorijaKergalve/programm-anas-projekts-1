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

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return "Šo burtu jūs jau minējāt."
        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            if self.is_word_guessed():
            
