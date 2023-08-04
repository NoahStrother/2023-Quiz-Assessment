import random
times_table = 5
answer = 0

print("Here is the {} times table".format(times_table))
for x in range(1,11):
    answer = x * times_table 
    print("{} times {} is {}".format(x,times_table,answer))
