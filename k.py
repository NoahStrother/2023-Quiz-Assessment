#import random
import random
def multiplication_gen():
  #Variables
  score = 0
  lives = 3
  rounds_played = 0

  #run the game until users plays all 10 rounds or loses all 3 lives
  while lives > 0 and rounds_played < 10:
    #generate two random numbers
    num1 = random.randint(1,10)
    num2 = random.randint(1,15)
    #User stats
    print()
    print(f"Score: {score}  Lives: {lives}")

      #increase # of rounds played
    rounds_played += 1
      #Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    #ask user the question
    print()
    print("What is", num1, "x" ,num2, "=")
    #user answer
    answer = input()
    #To check if answer is invalid or blank
    if not answer or not answer.isdigit():
      print("Invalid input. Please enter a number.") 
      lives -= 1
      print(f"Lives: {lives}")
      continue 
    #if answer is correct/incorrect  
    if int(answer) == num1 * num2:
      print("Correct!")
      score += 1
    else:
      print("Incorrect")
      print()
      print(f"The correct answer is {num1 * num2}")
      lives -= 1


    #amount of rounds_played
    rounds_played += 1

  #end game counclusion
  print()
  print("Game over")
  print()
  print(f"Rounds Played: {rounds_played}")
  print()
  print(f"Correct Answer: {score}")
  print()
  print(f"Lives Left: {lives}")

  print()
  print("Thank you for playing the Multiplication quiz")

multiplication_gen()