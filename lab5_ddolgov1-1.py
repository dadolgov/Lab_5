"""
Dice game
Author: Dmitrii Dolgov
Roll 2 dice, count the scores and print the funny names of combinations
"""

import random
command:str
print("Welcome to the Dice!")
print("Press Enter to roll, type 'Quit' and press enter to quit")
command=input("ARE YOU READY TO ROLL??? ")

while(command.capitalize()!="Quit"):
    die_1 : int = random.randint(1,6)
    die_2 : int = random.randint(1,6)
    total : int = die_1 + die_2

    print(f"\nYou rolled {total}!")
    print(f"Your dice are:")
    if total==12: 
        print(f"{die_1} & {die_2}: Boxcars!")
    elif total==11:
        print(f"{die_1} & {die_2}: Six Five no Jive!")
    elif total==10 and die_1==5:
        print(f"{die_1} & {die_2}: Puppy Paws!")
    elif total==9:
        print(f"{die_1} & {die_2}: Nina from Pasadena!")
    elif total==8 and die_1==4:
        print(f"{die_1} & {die_2}: Eighter from Decatur!")
    elif total==7 and (die_1==1 or die_2==1):
        print(f"{die_1} & {die_2}: Six Ace!")
    elif total==6 and die_1==3:
        print(f"{die_1} & {die_2}: Jimmy Hicks from the Sticks!")
    elif total==5:
        print(f"{die_1} & {die_2}: Little Phoebe!")
    elif total==4 and die_1==2:
        print(f"{die_1} & {die_2}: Little Joe from Kokomo!")
    elif total==3:
        print(f"{die_1} & {die_2}: Ace Caught a Deuce!")
    elif total==2:
        print(f"{die_1} & {die_2}: Snake Eyes!")
    else:
        print(f"{die_1} & {die_2}!")
    command=input("\nAnother one? ")

