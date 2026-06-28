
import numpy as np

def get_matrix():
    # Matrix A dimensions
    n = int(input("Enter number of rows in A: "))
    n_cols = int(input("Enter number of cols in A: "))
    
    matrix_A = []
    for i in range(n):
        row_A = list(map(int, input(f"  Row {i+1} of A: ").split()))
        if len(row_A) != n_cols:
            print(f" Enter exactly {n_cols} values!")
            return
        matrix_A.append(row_A)
    
    A = np.array(matrix_A)
    
    # Matrix B dimensions
    m = int(input("Enter number of rows in B: "))
    m_cols = int(input("Enter number of cols in B: "))
    
    matrix_B = []
    for j in range(m):
        row_B = list(map(int, input(f"  Row {j+1} of B: ").split()))
        if len(row_B) != m_cols:
            print(f" Enter exactly {m_cols} values!")
            return
        matrix_B.append(row_B)
    
    B = np.array(matrix_B)
    
    print(f"\nMatrix A:\n{A}")
    print(f"\nMatrix B:\n{B}")
    
    return A, B

def add(A,B):
    if(A.shape != B.shape):
        print("Shapes must be match for addition")  
        return
    else:
        return A + B 
def sub(A,B):
    if(A.shape != B.shape):
        print("Shapes must be match for subtraction ")  
        return
    else :
        return  A - B
def multi(A,B):
    if(A.shape[1]!=B.shape[0]):
        print(" Cols of A must equal Rows of B!")
        return
    return np.dot(A,B)
def transpose(matrix):
    return matrix.T
def det(matrix):
    if (matrix.shape[0]!=matrix.shape[1]):
        print("matrix must be squre matrix")
        return
    return np.linalg.det(matrix)
  
def display_result(operation_name,result):
    print("\n" + "="*50)
    print(f"operation:{operation_name}")
    if result is None:
        print("operation failed")
        print("="*50)
    else:
        print(result)
        print("="*50)
def main():
    print("\n" + "="*50)
    print("       MATRIX OPERATIONS TOOL")
    print("="*50)

    A, B = get_matrix()

    while True:
        print("\n------- MENU -------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose of A")
        print("5. Transpose of B")
        print("6. Determinant of A")
        print("7. Determinant of B")
        print("8. Exit")
        print("--------------------")

        choice = input("Choose (1-8): ")

        if choice == "1":
            display_result("Addition", add(A, B))
        elif choice == "2":
            display_result("Subtraction", sub(A, B))
        elif choice == "3":
            display_result("Multiplication", multi(A, B))
        elif choice == "4":
            display_result("Transpose A", transpose(A))
        elif choice == "5":
            display_result("Transpose B", transpose(B))
        elif choice == "6":
            display_result("Determinant A", det(A))
        elif choice == "7":
            display_result("Determinant B", det(B))
        elif choice == "8":
            print("\n✅ Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Enter 1-8 only.")

main()