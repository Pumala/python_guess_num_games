import random

def check_input():
    again = raw_input("Do you want to play again (Y or N)? ").lower()
    if again == "y" or again == "yes":
        return 5
    else:
        print "Bye!"

def play_me():
    print "I am thinking of a number between 1 and 10."
    random_num = random.randint(1, 10)
    count = 5

    while count >= 1:
        print "You have %d guesses left." % count
        guess = int(raw_input("What's the number? "))
        if (count == 1 or guess == random_num):
            if (guess == random_num):
                print "Yes! You win!"
            count = check_input()
            if count != 5:
                break
            else:
                print "I am thinking of a number between 1 and 10."
                random_num = random.randint(1, 10)
                count = 5
        elif guess < random_num:
            print "%d is too low." % guess
            count -= 1
        else:
            print "%d is too high." % guess
            count -= 1

play_me()
