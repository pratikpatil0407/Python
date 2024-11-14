import pandas as pd

# creating Dataframe
# You can create a DataFrame from a dictionary, a list, or a NumPy array.

data = {
    'Name' : ['Pratik','Prathamesh','Digambar'],
    'Age' : [19,20,21],
    'City': ['Kolhapur','Satara','Ajara']
}

df = pd.DataFrame(data)
print(df ,"\n")
print("--------------------------------")

# Accesing columns
ages = df['Age'] 
print(ages[1])
print(df ,"\n")
print("--------------------------------")

# setting indexes 
df.index = ['No_1','No_2','No_3']
print(df)
print("--------------------------------")

# Filtering data
fil_age = df[df['Age']>20]
print(fil_age)
print("--------------------------------")


# reading files using pandas
df1 = pd.read_excel('temp.xlsx')
print(df1)