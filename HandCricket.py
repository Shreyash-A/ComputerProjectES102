import random

#printing game rules

print("                Welcome")
print("Lets play Hand Cricket")
print("Winning Rules are as follows:")
print("You need to enter runs from 1 to 6 \n Then computer will choose a random number \n Whose number is greater WINS \n If both are equal you are out "  )

name = input("Enter your name:")
#taking user input

while True:
    print("Your choice \n 1. 1  \n 2. 2 \n 3. 3 \n 4. 4 \n 5. 5 \n 6. 6 \n ")
    userinput = int(input("Your turn: "))
    
    while userinput > 6 or userinput < 1:
        userinput= int(input("Please enter valid number :"))
        
    userinput = str(userinput)
    print("Your choice: " + userinput)
    print("\nNow computer's turn")
    
    #taking computer choice
    
    compChoice = random.randint(1, 6)
    compChoice = str(compChoice)
    
    print("Computer choice is: " + compChoice)
    print(userinput + " V/s " + compChoice)
    
    compChoice = int(compChoice)
    userinput = int(userinput)
    #deciding winner
    if compChoice >= userinput :
        print(" Computer Wins")
        print("Do you want to play again? (Y/N)")
        ans = input()
        if ans == 'n' or ans == 'N':
            break
       #declaring winner and asking to play again
    else:
        print(name, "WIN  CONGRATULATIONS")
        print("Do you want to play again? (Y/N)")
        ans = input()
        if ans == 'n' or ans == 'N':
            break

print("\nThanks for playing")
