import random

secretNumber = random.randint(1,10)
print ("I'm taking a guess between 1 to 10.")

for guessTaken in range(1,7):
    guess = int(input("Take a guess:"))

    if guess < secretNumber:
        print ("Your guess is too low.")
    elif guess > secretNumber:
        print ("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print ("You guessed it correct in {} guesses!".format(guessTaken))
else:
    print ("The number I was thinking of was {} !".format(secretNumber))