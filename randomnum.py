import random

min = int(input("What is the min?\n"))
max = int(input("What is the max?\n"))
def random_gen(min, max):
    number = random.randint(min, max)
    print("random number: " + str(number))

random_gen(min, max)

