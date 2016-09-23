import random

random_num = random.randint(1, 10)

print "I am thinking of a number between 1 and 10."

while random_num:
    guess = int(raw_input("What is the number? "))
    if guess == random_num:
        print "Yes! You win!"
        break
    elif guess < random_num:
        print "%d is too low." % guess
    else:
        print "%d is too high." % guess
