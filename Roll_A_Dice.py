import random

def RollDice(rolls):
    for i in range(0, rolls):
        number = random.randint(1, 6)
        print("---")
        print("-" + str(number) + "-")
        print("---")
        print()
    Menu()

def Menu():
    print("1.Roll a dice")
    print("2.Roll multiple dice")
    print("--------------------")
    print("3. Quit program")
    print("Exit program")
    choice = int(input("enter here: "))

    if(choice == 1):
        RollDice(1)
    if(choice == 2):
        rolls = int(input("How many rolls? "))
        RollDice(rolls)
    if(choice == 3):
        quit();

Menu()

