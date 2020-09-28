import random 
while True:
    print("welcome to Game \n Select options \n 1.Rock 2.Paper 3. Sissor")
    userchoice = int(input("Enter your options: "))
    while userchoice >3 or userchoice <1:
          userchoice = int(input("enter your valid option:"))
    if userchoice == 1:
       print("Rock")
       optionselected = "Rock"
    elif userchoice == 2:
         print("Paper")
         optionselected = "Paper"
    else:
       print("Sissor")
       optionselected = "Sissor"
    print("your selected option is:" +optionselected)
    print("Computer choice")
    cmchoice = random.randint(1,3)
    #print(cmchoice)
    while cmchoice == userchoice:
          cmchoice = random.randint(1,3)
          #print(cmchoice)
    if cmchoice == 1:
       print("Rock")

    elif cmchoice == 2:
         print("Paper")
    else:
        print("Sissor")
    if (cmchoice == 1 and userchoice == 2) or (cmchoice == 2 and userchoice == 1):
       #print("Paper")
       result = "Paper"
    elif (cmchoice == 2 and userchoice == 3) or (cmchoice == 3 and userchoice == 2):
        #print("Sissor")
        result = "Sissor"
    else:
       # print("Rock")
       result = "Roock"
    if optionselected == result:
       print("You win")
    else:
       print("computer wins")
    playagin = input("Do you want play again?Yes/No:")
    if playagin == "No":
       break











   




