import pandas as pd
import numpy as np

# Use forward slashes in the file path or use raw string
s = "C:\Users\Sriva\Downloads\Lab Session Data.xlsx"

# Load the correct sheet name
data = pd.read_excel(s, sheet_name='Purchase data')

# Extract relevant columns for matrix A
A = data[['Candies (#)', 'Mangoes (Kg)','Milk Packets (#)']].dropna()

rank_A = np.linalg.matrix_rank(A_matrix)
print(f'The rank of the matrix is {rank_A}')

inverse_A = np.linalg.pinv(A_matrix)
X_matrix = np.dot(inverse_A, C_matrix)

print(X_matrix)