import random
# Wordaholic - A simple word guessing game
word_bank = ['files', 'jungle', 'garden', 'magic', 'night']
word = random.choice(word_bank)

guessed_letters = ['_'] * len(word)
attempts = 5

# Game loop
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessed_letters))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
        print('Correct guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessed_letters:
        print('\nCongratulations! You guessed the word: ' + word)
        break

    if attempts == 0 and '_' in guessed_letters:
        print('\nGame Over! The word was: ' + word)
