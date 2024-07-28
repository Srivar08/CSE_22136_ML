def matrixmul(a, b):
    # Get the number of rows in matrix a
    m = len(a)
    # Get the number of columns in matrix a (and rows in matrix b)
    n = len(a[0])
    # Get the number of columns in matrix b
    p = len(b[0])

    # Check if the matrices can be multiplied
    if len(b) != n:
        return "Matrices are not multipliable"

    # Initialize the result matrix with zeros
    c = []
    for i in range(m):
        c.append([0] * p)

    # Perform matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c


def input_matrix(name):
    # Prompt user to enter the number of rows and columns for the matrix
    rows = int(input(f"Enter the number of rows for matrix {name}: "))
    cols = int(input(f"Enter the number of columns for matrix {name}: "))
    matrix = []

    print(f"Enter the elements for matrix {name} row-wise:")
    for i in range(rows):
        # Read a row of elements and split them into a list
        row = list(map(int, input().split()))

        # Check if the row has the correct number of columns
        if len(row) != cols:
            print(f"Error: Each row must have exactly {cols} elements.")
            return None

        # Add the row to the matrix
        matrix.append(row)

    return matrix


# Prompt user to input matrix A
print("Input matrix A:")
A = input_matrix("A")
if A is None:
    print("Invalid input for matrix A. Exiting.")
    exit()

# Prompt user to input matrix B
print("Input matrix B:")
B = input_matrix("B")
if B is None:
    print("Invalid input for matrix B. Exiting.")
    exit()

# Multiply matrices A and B
result = matrixmul(A, B)

# Check if the result is an error message or the resulting matrix
if type(result) == str:
    print(result)
else:
    print("Matrix AB:")
    for row in result:
        print(row)
