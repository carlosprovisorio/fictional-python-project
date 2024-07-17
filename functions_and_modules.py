# Defining Functions
def greet(name):
    return f"Hello, {name}!"


print(greet("Carlos"))


# Lambda Functions
add = lambda x, y: x + y
print(add(5, 3))


# Modules and Packages
# Creating a module(save as mymodule.py)
def say_hello(name):
    print(f"Hello, {name}!")


# using a module
import mymodule

mymodule.say_hello("Carlos")
