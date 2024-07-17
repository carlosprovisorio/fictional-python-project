# Reading and Writing files

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Working with CSV, JSON
import csv
import json

# Reading a CSV file
with open("data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"])


# Writing to a JSON file
data = {"name": "Carlos", "age": 39}
with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile)
