import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = './data/EN_Dataset/en_lpor_explorer.csv'

# Read csv
df = pd.read_csv(FILE_PATH)

# Display first all columns of the first 5 entries in the dataset
pd.set_option('display.max_columns', None)
print(df.head(), '\n')

# Display preliminary information about the dataset contents
print(df.info(), '\n')

# Display distribution of numerical data
print(df.describe(), '\n')

# Display counts of each type of value for each feature
for col in df.columns:
 print(df[col].value_counts(), '\n')

"""
Data Cleaning and Transformation 
"""

# Exclude data with missing values
df = df.dropna()

# Applying ___ transformation to data
df['severity'] = df['severity'].map({'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4})


"""
Data Visualization 
"""



"""
Hypothesis Testing
"""