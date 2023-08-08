import random
score = 0
for x in range(100):
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)
  print("What is ",num1,"+",num2,"=")
  user_answer = int(input(""))
  answer = num1 + num2
  if user_answer == answer:
    print("Correct!")
    score +=1
  else:
    print("Wrong!")
print("Your final score is: ", score)