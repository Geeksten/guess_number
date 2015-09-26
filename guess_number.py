#very basic guessing
from random import randint
# greet player
print "Howdy!"
# get player name
player_name = raw_input("Who do we have here? ")
#computer pick a random number between 1 and 100
#random.randint(a, b)
#Return a random integer N such that a <= N <= b
# have player choose random number between 1 and 100
number = randint(1, 101)
print number
print "{}, I am thinking of a number between 1 and 100, \nCan you guess it?".format (player_name.capitalize())
while True:
    #get guess
    guess = int(raw_input())
    #     if guess is incorrect:
#         give hint
    if guess < number:
        print "Your guess is too low! Guess again."
    elif guess > number:
        print "Your guess is too high! Guess again."
    else:
#         congratulate player
        print "Congratulations, your guess was right!"
        break
    