

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

# function to display instructions
def instructions():
  print("*** How to play ***\n")
  print("""Welcome to Noahs Math Quiz.
  If you get a math equation wrong you will lose.
  one of three lines.
  Good Luck!\n""")
  return ""


# *** MAIN ROUTINE ***
# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
# if user hasn't played before instructions are displayed
if played_before == "no":
   instructions()