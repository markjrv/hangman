import random
import time


name = input("enter your name: ")
print("welcome player", (name))
print("-------------------------------------------------------------")
print("try to guess the world less than 8 attempts")
print("Goodluck player")


# List of words to choose from
Listofanimals = ['dog','cat','bird','carabao','ants','fish','tiger','whale','octopus','chicken']


# Timer restriction (in seconds)
timer = 30

# Randomly select a word
word = random.choice(Listofanimals)

# Create a list of underscores the same length as the word
guessmade = ["_"] * len(word)

# Keep track of remaining guesses and incorrect guesses
remaining_guesses = 8
incorrect_guesses = []

# Start the timer
start_time = time.time()

while "_" in guessmade and remaining_guesses > 0 and time.time() - start_time < timer:
    # Print the current state of the word
    print(" ".join(guessmade))
    print("Incorrect guesses: " + " ".join(incorrect_guesses))
    print("Remaining guesses: " + str(remaining_guesses))
    print(f"Time Remaining: {timer-(time.time() - start_time):.2f}")

    # Get user's guess
    guess = input("\nGuess a letter: ").lower()


    # Check if the guess is in the word
    if guess in word:
        # Replace underscores with correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guessmade[i] = guess
    else:
        # Incorrect guess
        incorrect_guesses.append(guess)
        remaining_guesses -= 1

# Check if the user won or lost
if "_" not in guessmade:
    print(f"You win! The word was {word}")
    
elif remaining_guesses == 0:
    print(f"You lose! The word was {word} ")
else:
    print(f"Time's Up! The word was {word} ")


