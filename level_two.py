import random

user_number = input("Enter a number between 1-100: ")
int_number = int(user_number)

guess = 0

while guess < 5:
    random_guess = random.randint(1,101)
    print(random_guess)
    if random_guess == int_number:
        print("Comp was right!")
        break
    else:
        guess += 1
        print("Comp was wrong!")
