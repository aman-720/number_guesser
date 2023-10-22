import random

top_limit = input("Type a number: ")

if top_limit.isdigit():
    top_limit = int(top_limit)

    if top_limit <=0:
        print("give a number larger than zero(0)")
        quit()

else:
    print("we asked for a number :( }")
    quit()


random_number = random.randint(0, top_limit)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please give in a number.")
        continue

    if user_guess == random_number:
        print("Wohoo! you got it correct.")
        break
    else:
        if user_guess < random_number:
            print("you were above the number! ")
        else:
            print("you were below the number! ")

print("it took you", guesses, "guesses.")