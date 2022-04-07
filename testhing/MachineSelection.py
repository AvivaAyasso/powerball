import random         #Importing the random library / a  library that picks randomly from list
from colorama import init, Fore, Style  #Importing a color and design library
init()
from Game import User


class machineSelection(User):
    def __init__(self):
        super().__init__()



    machine = [] #An empty list that will be used to store the six winning numbers


    def randomSelection(self):
        machine = []  # An empty list that will be used to store the six winning numbers

        for i in range(5):              #A loop that runs in the range of one to twenty and randomly selects five numbers
            num = random.randint(1, 20)
            while num in machine:        #A loop that checks that the numbers do not repeat themselves...
                num = random.randint(1, 20)      #....and if so it repeats itself and replaces them
            machine.append(num)          #The numbers are added to the list
            machine.sort()               #The numbers are arranged in a list


        for j in range(1):
            gold = random.randint(1, 10)    #loop that runs in the range of one to ten and randomly selects one numbers
            machine.append(gold)        #The selected number is added to a list that already has the first five numbers
        return "Today's Powerball Winning Numbers are :"    #Prints the result of the machine lottery
        return (' '.join([str(num) if machine[0:5] in machine else f'{Fore.MAGENTA}{num}{Style.RESET_ALL}' for num in machine[0:5]]),
            ' '.join([str(machine) if machine in machine else f'{Fore.YELLOW}{machine[5]}{Style.RESET_ALL}']))
                                      #Remove markers and add colors to the printing






















