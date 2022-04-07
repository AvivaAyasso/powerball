import random

def pretty_print(num):
    print("*********************************")
    print("The numbers that came up in the lottery are :")
    print(num)
    print("*********************************")

def prettyPrint(num):
    print("*********************************")
    print("Your numbers that came up in the lottery are :")
    print(num)
    print("*********************************")


winning_numbers = []
for i in range(0, 5):
    num = random.randint(1, 20)
    while num in winning_numbers:
        num = random.randint(1, 20)
    winning_numbers.append(num)
    winning_numbers.sort()

for i in range(1):
    gold = random.randint(1, 10)
    winning_numbers.append(gold)

print(winning_numbers)



lucky_numbers = []
for i in range(0, 5):
    num = random.randint(1, 20)
    while num in lucky_numbers:
        num = random.randint(1, 20)
    lucky_numbers.append(num)
    lucky_numbers.sort()

for i in range(1):
    gold = random.randint(1, 10)
    lucky_numbers.append(gold)

print(lucky_numbers)




counter = 0
for num in winning_numbers:
    if num in lucky_numbers:
        counter = counter + 1

print("You guessed" +" "+ str(counter) +" "+ "numbers correctly")


