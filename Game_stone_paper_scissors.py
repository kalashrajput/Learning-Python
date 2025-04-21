#Making Stone, Paper and Scissors game :
import random
print("----- WELCOME TO THE GAME -----")
print('''
HERE ARE YOUR CHOICES -
      Press '1' for Stone
      Press '2' for Paper
      Press '3' for Scissors
      ''')
bhishika=int(input("Bhishika, enter the number of your choice - "))
kamles=random.randrange(1,4)
dict={"Stone":1,"Paper":2,"Scissors":3}
reversedict={1:"Stone",2:"Paper",3:"Scissors"}
print("Bhishika chose - ",reversedict[bhishika])
print("Kamles chose - ",reversedict[kamles])

if(bhishika==kamles):
    print("It's a DRAW!")
else:
    if((bhishika==1 and kamles==2) or (bhishika==2 and kamles==3) or (bhishika==3 and kamles==1)):
        print("Kamles wins!")
    else:
        print("Bhishika wins!")
print("Thank You For Playing :) ")