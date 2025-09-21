import random

OPERATORS = ["+","*","/","-"]
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
	
for i in range(TOTAL_PROBLEMS):
	express, answer = generate_problem()
	while True:
		guess = input("problem"+str(i+1)+ ":" +express+" " + "=")
		if guess == str(answer):
			break
			
