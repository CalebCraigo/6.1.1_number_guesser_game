import random

user_number = input("Enter a number between 1-100: ")
int_number = int(user_number)
# random_guess = random.randint(1,101)

high = 100
floor = 1

random_guess = (high + floor)/2


guess = 0

while guess < 5:
    print(random_guess)
    if random_guess == int_number:
        print("Comp was right!")
        break
    elif random_guess > int_number:
        high = random_guess
        random_guess = (high + floor)/2
        guess += 1
        print("Was too high!")
    elif random_guess < int_number:
        floor = random_guess
        random_guess = (high + floor)/2
        print("Was too low!")
        guess += 1


# for random_guess in range(5):
#     random_guess = random.randint(1,101)
# print(random_guess)
# if random_guess == int_number:
#     print("Comp was right!")
# elif random_guess > int_number:
#     print("Was too high!")
# elif random_guess < int_number:
#     print("Was too low!")

# random_number = random.randint(1,101)
# print(random_number)
# if random_number == int_guess:
#     print("Comp was right!")
# else:
#     print("Comp was wrong!")
