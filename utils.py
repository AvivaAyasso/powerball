import random

import colorama as colorama

# pip install colorama
from colorama import init, Fore, Style
init()



white_balls = [] #An empty list that will be used to store the six winning numbers


def whiteBalls():
    for i in range(5): #A loop that runs in the range of one to twenty and randomly selects five numbers
        num = random.randint(1, 20)
        while num in white_balls: #A loop that checks that the numbers do not repeat themselves
            num = random.randint(1, 20)
        white_balls.append(num) #The numbers are added to the list
        white_balls.sort() #The numbers are arranged in a list


#A run is made to select the strong number in the range of one to ten
    for j in range(1):
        gold = random.randint(1, 10)
        white_balls.append(gold)
    print("Today's Powerball Winning Numbers are :")
    print(' '.join([str(num) if white_balls[0:5] in white_balls else f'{Fore.MAGENTA}{num}{Style.RESET_ALL}' for num in white_balls[0:5]]),
        ' '.join([str(white_balls) if white_balls in white_balls else f'{Fore.YELLOW}{white_balls[5]}{Style.RESET_ALL}']))

powerball = []

def poewrball():
    for i in range(5):
        num = random.randint(1, 20)
        while num in powerball:
            num = random.randint(1, 20)
        powerball.append(num)
        powerball.sort()

    for j in range(1):
        gold = random.randint(1, 10)
        powerball.append(gold)
    print("Your lucky numbers are :")
    print(' '.join([str(num) if powerball[0:5] in powerball else f'{Fore.MAGENTA}{num}{Style.RESET_ALL}' for num in powerball[0:5]]),
          ' '.join([str(powerball) if powerball in powerball else f'{Fore.YELLOW}{powerball[5]}{Style.RESET_ALL}']))





def counter():
    counter = 0
    for a in white_balls[0:5]:
        for b in powerball[0:5]:
            if a == b:
                counter += 1


    flag = False
    if white_balls[5] == powerball[5]:
        flag = True


    if counter == 5:
        if flag == True:
            print("Jackpot you won 324,000,000$")
        else:
            print("You guessed 5 white balls but not the powerball, you won 1,000,000$")
    elif counter == 4:
        if flag == True:
            print("You guessed 4 white balls and the powerball, you won 10,000")
        else:
            print("You guessed 4 white balls but not the powerball, you won, you won 100$")
    elif counter == 3:
        if flag == True:
            print("You guessed 3 white balls and the powerball, you won 100$")
        else:
            print("You guessed 3 white balls but not the powerball, you won 7$")
    elif counter == 2:
        if flag == True:
            print("You guessed 2 white balls and the powerball, you won 7$")
        else:
            print("You guessed 2 white balls but not the powerball, you won 0$")
    elif counter == 1:
        if flag == True:
            print("You guessed 1 white balls and the powerball, you won 4$")
        else:
            print("You guessed 1 white balls but not the powerball, you won 0$")
    elif counter == 0:
        if flag == True:
            print("You did not guessed any white balls but you guessd the powerball, you won 4$")
        else:
            print("You did not guess any number, try again")











