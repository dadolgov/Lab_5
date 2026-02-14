"""
Dice game
Author: Dmitrii DOlgov
Roll 2 dice, count the scores and print the funny names of combinations
"""

import random

die_1 : int = random.randint(1,6)
die_2 : int = random.randint(1,6)
total : int = die_1 + die_2

print(die_1)
print(die_2)

if total==12: 
    print("Boxcars")
elif(total==11):
    print("Six Five no Jive")
elif total==10 and die_1==5:
    print("Puppy Paws")
elif total==9:
    print("Nina from Pasadena")
elif total==8 and die_1==4:
    print("Eighter from Decatur")
elif total==7 and (die_1==1 or die_2==1):
    print("Six Ace")
elif total==6 and die_1==3:
    print("Jimmy Hicks from the Sticks")
elif total==5:
    print("Little Phoebe")
elif total==4 and die_1==2:
    print("Little Joe from Kokomo")
elif total==3:
    print("Ace Caught a Deuce")
elif total==2:
    print("Snake Eyes")
