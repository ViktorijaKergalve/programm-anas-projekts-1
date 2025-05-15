import random

class WordList:
    def __init__ (self):
        self.words = ["skola", "saule", "draugi", "dators", "grāmata", "zirgs", "futbols", "grīda", "maize", "latviešu valoda"]

    def get_random_word(self):
      return random.choice(self.words)
