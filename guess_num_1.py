random_num = 5

print "I am thinking of a number between 1 and 10."

while random_num:
    guess = int(raw_input("What's the number? "))
    if guess == random_num:
        print "Yes! You win!"
        break
    else:
        print "Nope, try again."
