import random

def yes_no(question):
  
   valid = False
   while not valid:
      # asks user for input
      response = input(question).lower()
      # assesses response as yes/no or prompts correct input
      if response == "yes" or response == "y":
          response = "yes"
          return response
      elif response == "no" or response =="n":
          response = "no"
          return response
      else:
          print("Please enter yes or no ")

print("***Welcome To Noah's Math's Quiz***")
# function to display instructions
def instructions():
  print("*** How to play ***\n")
  print("""Instructions, 
  You will be asked practicly unlimited maths addition equations 
  unless you lose all three of your lifes, 
  If you get a math equation wrong you will loseone of three lines.
  Good Luck!\n""")
  return ""


# *** MAIN ROUTINE ***
# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
# if user hasn't played before instructions are displayed
if played_before == "no":
   instructions()

rounds_played = 0
score = 0
lives = 3
while lives > 0 and rounds_played < 10:
  for x in range(10):
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    rounds_played += 1
    print("What is ",num1,"+",num2,"=")
    user_answer = int(input(""))
    answer = num1 + num2
    if user_answer == answer:
      print("Correct!")
      score +=1
    else:
      print("Wrong!")
      lives -=1
      print(f"Lives: {lives}")

    if lives <= 0 :
     print("Game Over")
     break
print("Your final score is: ", score)