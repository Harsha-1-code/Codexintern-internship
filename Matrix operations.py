import numpy as np

def get_matrix_input(name):
    rows = int(input(f"Enter the number of rows for matrix {name}: "))
    cols = int(input(f"Enter the number of columns for matrix {name}: "))
    print(f"Enter the elements of matrix {name} row-wise (space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().strip().split()))
        if len(row) != cols:
            print(f"Error: Row {i + 1} must have {cols} elements.")
            return None
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    if matrix is not None:
        print("Result:")
        print(matrix)
    else:
        print("Invalid matrix operation.")

def main():
    print("Welcome to the Matrix Operations Tool")

    while True:
        print("\nChoose an operation:")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Transpose a matrix")
        print("5. Calculate determinant of a matrix")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            A = get_matrix_input("A")
            B = get_matrix_input("B")
            if A is not None and B is not None and A.shape == B.shape:
                result = A + B
                display_matrix(result)
            else:
                print("Error: Matrices must have the same dimensions for addition.")

        elif choice == '2':
            A = get_matrix_input("A")
            B = get_matrix_input("B")
            if A is not None and B is not None and A.shape == B.shape:
                result = A - B
                display_matrix(result)
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")

        elif choice == '3':
            A = get_matrix_input("A")
            B = get_matrix_input("B")
            if A is not None and B is not None and A.shape[1] == B.shape[0]:
                result = A @ B  # Using @ operator for matrix multiplication
                display_matrix(result)
            else:
                print("Error: Number of columns in A must be equal to number of rows in B for multiplication.")

        elif choice == '4':
            A = get_matrix_input("A")
            if A is not None:
                result = A.T
                display_matrix(result)

        elif choice == '5':
            A = get_matrix_input("A")
            if A is not None and A.shape[0] == A.shape[1]:
                result = np.linalg.det(A)
                print("Determinant:", result)
            else:
                print("Error: Determinant can only be calculated for square matrices.")

        elif choice == '6':
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 6.")
main()