# students_count = 1000  # integer
# rating = 4.99  # float
# is_published = True  # boolean
# course_name = "Python Programming"
# print(students_count)


# course = "Python Programming"
# print(len(course))
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])


# Scape sequence in Python
# \"
# \'
# \\
# \n

# course = 'Python "Programming'
# print(course)

# first = "Carlos"
# last = "Ferreira"
# # full = first + " " + last     # Ugly
# full = f"{first} {last}"  # better version
# print(full)

# course = "  python programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.rstrip())
# print(course.find("Pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)


# x = 1 #integer
# x = 1.1 # float
# x = 1 + 2j # complex number

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10**3)

# x = 10
# x = x + 3
# x += 3


# import math

# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))

# x = input("X: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# bool(0) False
# bool(1) True
# bool(-1) True
# bool(5) True
# bool("") False
# bool("False") True

# print(10 > 3)
# print(10 >= 3)
# print(10 < 3)
# print(10 <= 3)
# print(10 == 10)
# print(10 == "10")
# print(10 != "10")
# "bag" > "apple"
# "bag" == "BAG"

temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
