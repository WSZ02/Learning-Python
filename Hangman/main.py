import random
from Hangman_visual import logo
from Hangman_visual import stages
from Hangman_words import word_list

random_word = random.choice(word_list)
random_word_length = len(random_word)

end_of_game = False
lives = 6

print(logo)

display = []

for _ in range(random_word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(random_word_length):
        letter = random_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])
