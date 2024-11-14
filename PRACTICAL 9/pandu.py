import pandas as pd

# create a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
       'Age': [25, 30, 35],
       'City': ['New York', 'London', 'Paris']}

# create a dataframe from the dictionary
df = pd.DataFrame(data)

print(df)
