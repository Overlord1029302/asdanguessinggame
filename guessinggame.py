import random

def guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 6
    previous_guesses = set()

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 20. You have 6 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            if guess in previous_guesses:
                print("You already guessed that number. Try a different one.")
                continue

            previous_guesses.add(guess)

            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number: {secret_number}")
                break

            attempts -= 1

            if guess < secret_number:
                print(f"Too low! You have {attempts} guesses remaining.")
            else:
                print(f"Too high! You have {attempts} guesses remaining.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")

    else:
        print(f"Sorry, you've run out of guesses. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
