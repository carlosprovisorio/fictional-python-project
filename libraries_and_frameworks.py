# NumPY
import numpy as np

array = np.array([1, 2, 3, 4])
print(array * 2)


# Pandas
import pandas as pd

data = {"Name": ["Carlos", "John"], "Age": [30, 25]}
df = pd.DataFrame(data)
print(df)

# Matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()

# Requests
import requests

response = requests.get("https://api.github.com")
print(response.json())

# Flask/Django
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
