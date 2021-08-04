import sys
import random

# Greet the user : )

name = input ("What's your name?\n")

def run ():
    choice = input (f"Hello, {name}, wanna play a game? y/n\n")
    if "y" in choice: 
        print ("Great! Let's play hangman")
    if "n" in choice:
        print ("Bye bye!")
        sys.exit()

# Defining bag of words
    bag_of_words = ["python", "machinelearning", "looping", "whileloop", "forloop", "programmer", "parameters", "deeplearning", "algorithms", "normalization", "exception", "modeling" ]
    
# Random secret word selected
    word = random.choice(bag_of_words)

# Create empty variable for guesses
    guesses = " "

#Total number of turns
    turns = 10

# Create while loop for turns and check if number is greater than 0
    while turns > 0:

    # Make a failed counter
        failed = 0

        for char in word:
        # Print if character is in the guess
            if char in guesses:
                print (char)
        # If not, print dash
            else:
                print ("-")
        #And increase fail counter by 1
                failed += 1

        # If failed equals zero, you won
        if failed == 0:
            print ("You won!")
            choice = input ("Would you like to play again? y/n\n")
            if "y" in choice:
                run()
            elif "n" in choice:
                sys.exit()
            else:
                print ("Ummm hello? Type y or n.")
       
        # Ask user to guess character
        guess = input ("Guess a character: ")

        # Set player guess to guesses
        guesses += guess

        # If guess not found in word
        if guess not in word:
            # Number of turns increases by 1
            turns -= 1
            print ("Wrong guess...this rope is getting a little tight")

            # How many turns left?
            print (f"You now have {turns} more guesses.")

            # If turns equals zero, game over
            if turns == 0:
                # You lose
                print ("The hangman has been hung...you lose")
                choice = input ("Would you like to play again? y/n\n")
                if "y" in choice:
                    run()
                elif "n" in choice:
                    sys.exit()
                else:
                    print ("Ummm hello? Type y or n.")
run ()
