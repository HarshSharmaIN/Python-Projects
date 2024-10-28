import random

def hangman():
    word_list = ["python", "java", "javascript", "c++", "ruby"]
    chosen_word = random.choice(word_list)
    word_letters = set(chosen_word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('Lives remaining:', lives)
        print('Used letters:', ' '.join(used_letters))

        print('\nCurrent word:')
        for letter in chosen_word:
            if letter in used_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print('You already used that letter. Guess again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died, sorry. The word was', chosen_word)
    else:
        print('You guessed the word', chosen_word, '!')

hangman()