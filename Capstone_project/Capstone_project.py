#Importing necessary libraries
import pandas as pd
import numpy as np

#Loading the dataset 
df = pd.read_csv('C:\\Users\\DELL\\Desktop\\Capstone\\Salary_Data (1).csv')
print(df.head())

#Show the initial missing values 
print('Missing values in each column')
print(df.isnull().sum())

# 1. Fill missing numeric values with mean 
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Years of Experience'].fillna(df['Years of Experience'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# 2. Fill missing categorical values with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Education Level'].fillna(df['Education Level'].mode()[0], inplace=True)
df['Job Title'].fillna(df['Job Title'].mode()[0], inplace=True)

# 3. Replace infinite values with NaN and handle them
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 4. Remove duplicate records
df.drop_duplicates(inplace=True)

# 5. Replace negative salaries with the mean salary
df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])

# 6. Remove outliers from salary using 3 standard deviation
salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - 3 * salary_std
upper_bound = salary_mean + 3 * salary_std
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# Show missing values after cleaning
print("Missing values after cleaning:\n", df.isnull().sum())

# Save the cleaned dataset
df.to_csv('Cleaned_Salary_Data.csv', index=False)
print('Data cleaning completed! Cleaned dataset saved as "Cleaned_Salary_Data.csv"')