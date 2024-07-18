# Try, Except Blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# Finally Clause
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()


# Raising Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return age


try:
    check_age(16)
except ValueError as e:
    print(e)
