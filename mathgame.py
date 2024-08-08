import random
import time

# List of operators to use in the problems
OPERATORS = ["+", "-", "*"]
# Change the minimum and maximum values for the operands
MIN_OPERAND = 0
MAX_OPERAND = 10
# Total number of problems the user will solve
TOTAL_PROBLEMS = 5

# Function to generate a random math problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random number for the left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random number for the right operand
    operator = random.choice(OPERATORS)  # Randomly select an operator

    expr = str(left) + " " + operator + " " + str(right)  # Create the math expression as a string
    answer = eval(expr)  # Evaluate the expression to get the correct answer
    return expr, answer  # Return both the expression and the answer

# Counter for tracking wrong answers
wrong = 0
input("Press enter to start!")  # Wait for the user to press Enter to start the game

print("----------------------")

start_time = time.time()  # Record the start time of the game

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a new problem
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  # Ask the user for their answer
        if guess == str(answer):  # If the guess is correct
            break  # Move to the next problem

        wrong += 1  # If the guess is wrong, increase the wrong answer counter

end_time = time.time()  # Record the end time of the game
total_time = round(end_time - start_time, 2)  # Calculate the total time taken

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")  # Display the total time taken


