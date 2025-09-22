import random
import time

OPERATORS = ["+","*","-"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
	left = random.randint(MIN_OPERAND,MAX_OPERAND)
	right = random.randint(MIN_OPERAND,MAX_OPERAND)
	operators = random.choice(OPERATORS)

	express = str(left) + " "+operators+ " " + str(right)
	answer = eval(express)
	return express, answer

wrong = 0
input("press enter for start")
start = time.time()	
			
for i in range(TOTAL_PROBLEMS):
	express, answer = generate_problem()
	while True:
		guess = input("problem"+str(i+1)+ ":" +express+" " + "=")
		if guess == str(answer):
			break
		else:
			wrong +1

end = time.time()
total_time = end - start
print("you taken",round(total_time,2),"seconds")
