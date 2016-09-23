import random

random_num = random.randint(1, 10)
count = 5

print "I am thinking of a number between 1 and 10."

while count >= 0:
    print "You have %d guesses left." % count
    guess = int(raw_input("What's the number? "))
    count -= 1
    if guess == random_num:
        print "Yes! You win!"
        break
    elif count == 0:
        print "You ran out of guesses!"
        break
    elif guess < random_num:
        print "%d is too low." % guess
    else:
        print "%d is too high." % guess
