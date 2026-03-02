import pandas as pd
print(pd.__version__)



# Create a dictionary with some data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Gokul","Brightson", "Nithish"],
    "Age": [25, 30, 35, 40, 26, 24, 23],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Texas", "New jersey", "california" ],
    "Salary": [70000, 80000, 90000, 100000, 500000, 500000, 500000]
}

# Convert dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Show the data
print(df)
print("")
print(df.head(2))
print("")
print(df.tail())
print("")
print(df.describe())
print("")
print(df.info())
print("")
print(df.shape)   
print("")
print(df.loc[2])
