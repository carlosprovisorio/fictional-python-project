# Conditional Statements
if age > 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")


# Loops

# For Loop
for i in range(5):
    print(i)


# While Loop
count = 0
while count < 5:
    print(count)
    count += 1


# Control Statements
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # stop loop
    print(i)
