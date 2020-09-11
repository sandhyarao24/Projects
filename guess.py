import random
while True:
   print("Welcome to Guess the Number")
   guess = int(input("Enter a number b/w 0-10:"))
   print("Computer choice")
   cmchoice = random.randint(0,10)
   print(cmchoice)
   if guess == cmchoice:
      print("You guess correct number")
   else:
      print("Try again")
   again = input("Do you want try again?Y/N:") 
   if again == "N" or again == "n":
      print("Thank you for playing")
      break
      



