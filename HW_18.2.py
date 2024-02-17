# Define a class named Functor
class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        # Check if the provided number is not positive
        if number <= 0:
            # Raise a ValueError if the number is not positive
            raise ValueError("The number must be positive")
        else:
            return number


# Define a function named is_positive
def is_positive(num):
    return num


my_func = Functor(is_positive)
result = my_func(17)
print(result)
