import random
from hangman_words import word_list

display = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
nr_lives = 6
end_of_game = False

for number in range(word_length):
    display.append("_")
print(display)
    
blank = "_"

while not end_of_game:
    guess = input("Pick a letter\n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in chosen_word:
        nr_lives -= 1
        print(display)
        if nr_lives == 0:
            end_of_game = True
            print("You lose")   
    if blank not in display:
        end_of_game = True
        print("You win")

        
#print(chosen_word.find(guess))