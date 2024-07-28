def transpose(matrix, rows, cols):
    # Initialize the transposed matrix with dimensions cols x rows
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Perform the transposition
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# Prompt user to input the number of rows and columns for the matrix
rows = int(input("Enter the number of rows of the matrix: "))
cols = int(input("Enter the number of columns of the matrix: "))
matrix = []

# Prompt user to input the elements of the matrix
print("Enter the elements of the matrix: ")
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(int(input(f"Element [{i + 1}][{j + 1}]: ")))
    matrix.append(a)

# Transpose the matrix
transposed = transpose(matrix, rows, cols)

# Print the transposed matrix
print("\nTransposed matrix:")
for row in transposed:
    print(row)

