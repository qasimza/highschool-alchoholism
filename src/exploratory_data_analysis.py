import pandas as pd

FILE_PATH = '../data/EN_Dataset/en_lpor_explorer.csv'

# Read csv
df = pd.read_csv(FILE_PATH)

# Display first all columns of the first 5 entries in the dataset
pd.set_option('display.max_columns', None)
print(df.head(), '\n')

# Display preliminary information about the dataset contents
print(df.info())

# Display distribution of data
print(df.describe())