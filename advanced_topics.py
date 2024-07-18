# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print(i)


# Content Managers
with open("example.txt", "w") as file:
    file.write("Hello, World!")
