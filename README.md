#main.py
from word_data import WordList
from game_logic import WordGame

def main():
  word_list = WordList()
  secret_word = word_list.get_random_word()
  game = WordGame( secret_word)

  print("Laipni lūgts spēlē Uzmini vārdu!")
  while not game.is_word_guessed() and game.tries_left > 0:
        print("\nVārds: ", game.display_word())
        guess = input( " Ievadi burtu:").lower()
        if len(guess) ! = 1 or not guess.isalpha():
            print (" Ievadi tikai vienu burtu! ")
            continue
