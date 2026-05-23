import random
def hangman():
    #Five prefined words per CoadAlpha scope
    words = ["python","programming","language","internship","hangman"]
    chosen_word = random.choice(words)
    attempts = 6 #limit incorrect guesses to 6
    guessed_letters = set()
    display = ["_"] *len(chosen_word)
    print("Welcome to hangman (coadalpha task 1)!")
    while attempts > 0 and "_" in display:
        print("\nword:"," ".join(display))
        print("attempts left:", attempts)
        guess = input("enter a single letter: ").lower().strip()
        if not guess.isalpha() or len(guess)!=1:
            print("please enter exactly one alphabet letter.")
            continue
        if guess in guessed_letters:
            print("you already tried that letter.")
            continue
        guessed_letters.add(guess)
        if guess in chosen_word:
            for i, ch in enumerate(chosen_word):
                if ch == guess:
                    display[i] = guess
            print("correct!")
        else:
            attempts -= 1
            print("wrong guess.")
    if "_" not in display:
        print(f"you won! the word was: {chosen_word}")
    else:
        print(f"game over! the word was: {chosen_word}")
if __name__=="__main__":
    hangman()