# Define the decorator function
def decorator(func):
    # Define the wrapper function inside the decorator
    def wrapper(num):



# Apply the decorator to the function is_positive
@decorator
def is_positive(num):
    # Simply return the number
    return num