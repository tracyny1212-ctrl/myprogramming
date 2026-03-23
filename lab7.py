
# Student ID: 6309037
#Component A
def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)
    print()


def main():
    # Personalization values from ID
    d1 = 7
    d2 = 3
    k = (d1 + d2) % 4 + 2   # 4
    shift = d1 - d2          # 4
    rows_keep = (d1 % 2) + 2 # 3

    # Non-square matrix (2 rows x 5 columns)
    matrix = [
        [5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50]
    ]

    # Print original matrix and dimensions
    print_matrix(matrix, "Original rectangular matrix:")
    print("Dimensions:")
    print("Rows =", len(matrix))
    print("Columns =", len(matrix[0]), "\n")

    # Last column
    last_column = [row[-1] for row in matrix]
    print("Last column:", last_column)

    # Sub-array with all rows, first 3 columns
    first_3_cols = [row[:3] for row in matrix]
    print("All rows, first 3 columns:")
    for row in first_3_cols:
        print(row)

    # Component B: ID-based modification
    chosen_row = d1 % len(matrix)  # 7 % 2 = 1 → second row
    old_row = matrix[chosen_row][:]

    # Replace entire row with values increased by k
    new_row = [value + k for value in old_row]
    matrix[chosen_row] = new_row

    # Starting column for sliced sub-array
    start_col = d2 % 2  # 3 % 2 = 1 → second column
    sliced_subarray = [row[start_col:] for row in matrix]

    # Print chosen row info
    print("\nChosen row index:", chosen_row)
    print("Old row:", old_row)
    print("New row:", new_row)

    # Print matrix after modification
    print_matrix(matrix, "Matrix after row replacement:")

    # Print sliced sub-array
    print("Sliced sub-array from starting column", start_col)
    for row in sliced_subarray:
        print(row)

    # Explanation of selections
    print("\nExplanation of choices based on Student ID:")
    print(f"- Chosen row = d1 % number_of_rows = 7 % 2 = {chosen_row} (second row)")
    print(f"- Starting column = d2 % 2 = 3 % 2 = {start_col} (second column)")
    print(f"- Each value in chosen row increased by k = {k}")


if __name__ == "__main__":
    main()