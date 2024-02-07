import pandas as pd

# Load the data from the provided Excel file
file_path = 'american_tennis.xlsx'
wimbledon_data = pd.read_excel(file_path)


# Display the first few rows of the dataframe to understand its structure
wimbledon_data.head()

# Step 2: Data Cleaning and Preparation

# Checking for missing values in the dataset
missing_values = wimbledon_data.isnull().sum()

# Checking for duplicate rows in the dataset
duplicate_rows = wimbledon_data.duplicated().sum()

# Checking for unique values in 'match_id' to see how many matches we have
unique_matches = wimbledon_data['match_id'].nunique()

# Checking for any inconsistencies in player names
unique_player1 = wimbledon_data['player1'].unique()
unique_player2 = wimbledon_data['player2'].unique()

# Let's print out the findings
print(f"Missing Values:\n{missing_values}\n")
print(f"Duplicate Rows: {duplicate_rows}\n")
print(f"Number of Unique Matches: {unique_matches}\n")
print(f"Unique Player 1 Names: {unique_player1}\n")
print(f"Unique Player 2 Names: {unique_player2}\n")

# If there are any missing values, we will need to decide on how to handle them.
# This could involve filling them in with a default value, such as 0 for numerical columns or 'Unknown' for categorical columns,
# or it might involve dropping rows or columns with missing values if they are not crucial for the analysis.

# For the purpose of this demonstration, let's assume we want to fill missing numeric values with 0
# and categorical values with 'Unknown'. Also, let's remove any duplicate rows if they exist.

# Filling missing numeric values with 0
numeric_columns = wimbledon_data.select_dtypes(include=['float64', 'int64']).columns
wimbledon_data[numeric_columns] = wimbledon_data[numeric_columns].fillna(0)

# Filling missing categorical values with 'Unknown'
categorical_columns = wimbledon_data.select_dtypes(include=['object']).columns
wimbledon_data[categorical_columns] = wimbledon_data[categorical_columns].fillna('Unknown')

# Dropping duplicate rows if any
if duplicate_rows > 0:
    wimbledon_data = wimbledon_data.drop_duplicates()

# Re-checking for missing values and duplicate rows after cleaning
missing_values_after = wimbledon_data.isnull().sum()
duplicate_rows_after = wimbledon_data.duplicated().sum()

# Display the cleaning results
print(f"After Cleaning - Missing Values:\n{missing_values_after}\n")
print(f"After Cleaning - Duplicate Rows: {duplicate_rows_after}\n")

cleaned_file_path = 'american_clean_data.csv'  # 指定保存文件的路径
wimbledon_data.to_csv(cleaned_file_path, index=False)