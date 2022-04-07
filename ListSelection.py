import random                                 # Importing the random library / a  library that picks randomly from list
from colorama import init, Fore, Style        # Importing a color and design library
init()

from Game import Game


class listSelection(Game):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)

    def randomSelection(self):
        list1 = []                   # An empty list that will be used to store the six winning numbers
        for i in range(5):          # A loop that runs in the range of one to twenty and randomly selects five numbers
            num = random.randint(1, 20)
            while num in list1:                  # A loop that checks that the numbers do not repeat themselves...
                num = random.randint(1, 20)  # ....and if so it repeats itself and replaces them
            list1.append(num)                    # The numbers are added to the list
        list1 = sorted(list1,reverse=False)                 # The numbers are arranged in a list

        for j in range(1):
            gold = random.randint(1, 10)            # loop that runs in the range of one to ten and randomly selects one numbers
            list1.insert(5,gold)                       # The selected number is added to a list that already has the first five numbers
        return list1 # Prints the result of the list lottery

        # Remove markers and add colors to the printing
    def color(self):
        balls = self.randomSelection()
        whiteballs = str(balls[0:5])
        goldball = str(balls[-1])
        print(Fore.MAGENTA+whiteballs+Style.RESET_ALL,Fore.YELLOW+goldball+Style.RESET_ALL)


    def compare_calculate(self):
        compare = 0
        flag = False
        user_list = self.randomSelection()
        machine_list = self.randomSelection()
        for a in user_list[0:5]:
            for b in machine_list[0:5]:
                if a == b:
                    compare += 1
        if user_list == machine_list[-1]:
            flag = True

        if compare == 5:
            if flag == True:
                print( "Jackpot you won 324,000,000$")
            else:
                print ("You guessed 5 white balls but not the powerball, you won 1,000,000$")
        elif compare == 4:
            if flag == True:
                print ("You guessed 4 white balls and the list, you won 10,000")
            else:
                print ("You guessed 4 white balls but not the powerball, you won, you won 10 $")

        elif compare == 3:
            if flag == True:
                print ("You guessed 3 white balls and the list, you won 100$")
            else:
                print ("You guessed 3 white balls but not the powerball, you won 7$")
        elif compare == 2:
            if flag == True:
                print ("You guessed 2 white balls and the list, you won 7$")
            else:
                print ("You guessed 2 white balls but not the powerball, you won 0$")
        elif compare == 1:
            if flag == True:
                print ("You guessed 1 white balls and the list, you won 4$")
            else:
                print ("You guessed 1 white balls but not the powerball, you won 0$")
        elif compare == 0:
            if True == flag:
                print("You did not guessed any white balls but you guessd the list, you won 4$")
            else:
                print ("You did not guess any number, try again")

    def __str__(self):
        return str(self.randomSelection()) +" "+ str(self.color()) +" "+str(self.compare_calculate())
