import random

def words(words_hangman):
    try:
        with open("words_hangman.txt" , 'r' ) as file:
            words = file.read().splitlines()
        return words
    except Exception as exc:
        print("Error : ",exc)
        return[]

def hangman():
    words_list = words("words.txt")
    if not words_list:
        return

    word = random.choice(words_list).lower()
    word_letters = list(word)
    guessed_letter = []
    tries = 10
    display = ['_'] * len(word)

    print("Welcome to Hangman \n Let's Start ")

    while tries > 0 and '_' in display:
        print("\nWord:",' '.join(display))
        print(f'Tries left : {tries}')
        guess = input("Guess a letter : ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter. ")
            continue
        if guess in guessed_letter:
            print("You have already guessed that letter.")
            continue

        guessed_letter.append(guess)
        
        if guess in word_letters:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Correct!!")
           
        else:
            tries -= 1
            print("Wrong Guess.")


    if '_' not in display :
        print("\n❁Congratulations! ´◡` ❁\n You have guessed the word ",word)

    else:
        print("\n❁You lost! ❁The word was : ",word)

hangman()








        
