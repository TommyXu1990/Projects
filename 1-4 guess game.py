answer = "2"
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = ""

Greeting = input("Hello! What is your name?: ")
if str(Greeting.lower()) == "alex":
    print("You suck Alex, you have 3 attempts to guess a number between 1 and 4.")
else:
    print("Welcome " + Greeting + "! I hope you enjoy this game! You have 3 attempts to guess a number between 1 and 4.")

while guess != answer and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Please enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("You ran out of guesses! You lose!")
else:
    print("You guessed correctly! The answer is " + str(answer) + "!")