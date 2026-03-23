# Student ID: 6309037

def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()

def main():
    # Personalization values
    d1 = 7
    d2 = 3
    k = (d1 + d2) % 4 + 2  # 4
    shift = d1 - d2         # 4
    rows_keep = (d1 % 2) + 2  # 3

    # Original matrix
    matrix = [
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ]

    # Print original matrix
    print_matrix(matrix, "Original matrix:")

    # Determine which row and column to modify
    row_index = d1 % len(matrix)  # 7 % 3 = 1 → second row
    col_index = d2 % len(matrix[0])  # 3 % 4 = 3 → fourth column
    print(f"Row to modify (row_index): {row_index}")
    print(f"Column to modify (col_index): {col_index}")

    # Modify row: add shift
    for j in range(len(matrix[row_index])):
        matrix[row_index][j] += shift

    # Modify column: multiply by k
    for i in range(len(matrix)):
        matrix[i][col_index] *= k

    # Print modified matrix
    print_matrix(matrix, "Modified matrix:")

if __name__ == "__main__":
    main()

"""the ouput:
Original matrix:
[21, 22, 23, 24]
[25, 26, 27, 28]
[29, 30, 31, 32]

Row to modify (row_index): 1
Column to modify (col_index): 3

Modified matrix:
[21, 22, 23, 96]
[29, 30, 31, 128]
[29, 30, 31, 128]"""