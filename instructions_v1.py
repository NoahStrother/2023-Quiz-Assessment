import random
# Create a yes and no function
def yes_no(question):
  valid=False
  while not valid:
    response = input(question).lower()
    # If they say yes, output 'program continues'
    if response == "yes" or response == "y":
      response="yes"
      return response         
    elif response == "no" or response == "n":
      response = "no"
      return response    
  # If they say no, output 'display instructions'  
    else:
      print("Please answer yes / no")

# main routine
show_instructions = ""
while show_instructions.lower() != "xxx":
  show_instructions = yes_no("Have you played this game before? ")
  if show_instructions == "no":
    print("display instructions")
  elif show_instructions == "yes":
    print("program continues")
    
print("Welcome To Noah's Math Quiz")\

def instructions():
  print("")
  print("Instructions")
  print()
  print("Here are the rules")
  print()
  print("You will be asked a number of maths questions")
  print()
  print("You will have three lives")
  print()
  print("When you get a question wrong you will lose a life")
