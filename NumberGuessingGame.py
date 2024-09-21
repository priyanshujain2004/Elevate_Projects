import random

def number_guessing_game():
    """
    This function implements a number guessing game where the computer
    generates a random number and the user has to guess it within a
    limited number of attempts.
    """

    lower_bound = 1  # Set the lower bound of the random number range
    upper_bound = 100  # Set the upper bound of the random number range
    max_attempts = 10  # Set the maximum number of attempts allowed

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"You got it in {attempts} attempts!")
            return

    print(f"You're out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()