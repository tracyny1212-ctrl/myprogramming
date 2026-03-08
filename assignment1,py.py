# Question 1
# Task 1 - Code (original idea with fixed syntax)
def number_checker(n):  # name of function
    if n == 0:
        return "Zero"
    elif n > 0:  # elif used since there is more than 1 condition
        return "Positive"
    else:
        return "Negative"

#Task 2-understanding
# This function checks if a number is positive, negative, or zero.
# It uses conditional statements (if, elif, else).
# First it checks if the number is equal to 0.
# If it is greater than 0 it returns "Positive".
# Otherwise the number must be negative, so it returns "Negative".
# Task 3 - Modification
# I modified the function by adding validation to make sure
# the input is actually a number before checking it.

def number_checker_modified(n):
    if not isinstance(n, (int, float)):
        return "Invalid input"
    if n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Negative"

# Question 2
# Task 1 - Code

def star_function(n):
    for i in range(1, n + 1):
        print("*" * i)


# Task 2 - Understanding
# This function prints a star pattern using a for loop.
# The loop runs from 1 to the number given by the user.
# Each time the loop runs, it prints a number of stars equal
# to the loop number.

# Task 3 - Modification
# I modified the function by adding a condition that checks
# if the number of rows is greater than 0.

def star_function_modified(n):
    if n <= 0:
        print("Number must be greater than 0")
    else:
        for i in range(1, n + 1):
            print("*" * i)

# Question 3
# Task 1 - Code

def return_3(limit):
    num = 1
    while num <= limit:
        if num % 3 == 0:
            print("Multiple of 3")
        else:
            print(num)
        num += 1


# --------------------------------------------------
# Task 2 - Understanding
# --------------------------------------------------
# This function uses a while loop to count numbers from 1
# up to the limit entered by the user.
# The program checks if the number is divisible by 3 using
# the modulus operator (%).
# If the remainder is 0, it prints "Multiple of 3".
# Otherwise it prints the number.

# Task 3 - Modification: I modified the function by checking if the limit is positive.

def return_3_modified(limit):
    if limit <= 0:
        print("Limit must be greater than 0")
    else:
        num = 1
        while num <= limit:
            if num % 3 == 0:
                print("Multiple of 3")
            else:
                print(num)
            num += 1

# Question 4
# Task 1 - Code

def sum_of_even_numbers(start, end):
    total = 0
    for n in range(start, end + 1):
        if n % 2 == 0:
            total += n
    return total

# Task 2 - Understanding
# This function calculates the sum of all even numbers
# between a starting value and an ending value.
# The loop goes through each number in the range.
# If the number is even (divisible by 2), it is added
# to the total variable.
# Task 3 - Modification- I modified the function by adding a check to make sure the 
# start value is smaller than the end value.

def sum_of_even_numbers_modified(start, end):
    if start > end:
        return "Start value must be smaller than end value"

    total = 0
    for n in range(start, end + 1):
        if n % 2 == 0:
            total += n
    return total


if __name__ == "__main__":

    n = int(input("Enter a number for function 1: "))
    rows = int(input("Enter a number for function 2: "))
    limit = int(input("Enter a number for function 3: "))
    start = int(input("Enter a start value: "))
    end = int(input("Enter an ending value: "))

    print(number_checker(n))
    star_function(rows)
    return_3(limit)
    print(sum_of_even_numbers(start, end))