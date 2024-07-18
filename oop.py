# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


p1 = Person("Carlos", 39)
p1.greet()


# Inheritance
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


emp = Employee("Carlos", 39, "E123")
emp.greet()


# Polymorphism
class Bird:
    def sound(self):
        return "Chirp"


class Dog:
    def sound(self):
        return "Bark"


def make_sound(animal):
    print(animal.sound())


bird = Bird()
dog = Dog()
make_sound(bird)
make_sound(dog)


# Encapsulation
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = Account("Carlos", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
