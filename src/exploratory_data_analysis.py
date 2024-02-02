import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Preliminary visualization
sns.pairplot(df, x_vars={'Alcohol_Weekdays', 'Alcohol_Weekends', 'Grade_1st_Semester', 'Grade_2nd_Semester'})
plt.show()

"""
Data Cleaning and Transformation 
"""

# Applying ordinal encoding transformation to data
parent_education_mapping = {'na': 0, 'Primary School': 1, 'Lower Secondary School': 2, 'High School': 3,
                            'Higher Education': 4}
df['Mother_Education'] = df['Mother_Education'].fillna(0).map(parent_education_mapping)
df['Father_Education'] = df['Father_Education'].fillna(0).map(parent_education_mapping)
df['Father_Education'] = df['Father_Education'].map(parent_education_mapping)


"""
Data Visualization 
"""



"""
Hypothesis Testing
"""