# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares_difference(max_num):
    # for each number in range to the max_num argument, square and save in the list.  
    sum_squares = [num ** 2 for num in range(1, max_num+1)]

    # Use the sum function to get the total of the sum_squares.
    sum_squares_total = sum(sum_squares)

    # Add all numbers in range to passed in max_num, then square the total.
    squared_sum = (sum(range(1, max_num+1))) ** 2

    return squared_sum - sum_squares_total


print(sum_of_squares_difference(100))