# Regular function to add two numbers
def add(x, y):
    return x + y

# Lambda function to add two numbers
add_lambda = lambda x, y: x + y

# Testing the functions
num1 = 10
num2 = 5

# Using the regular function
result_function = add(num1, num2)
print(f"Result using regular function: {result_function}")

# Using the lambda function
result_lambda = add_lambda(num1, num2)
print(f"Result using lambda function: {result_lambda}")
""" 
# Output
# Result using regular function: 15
# Result using lambda function: 15
"""