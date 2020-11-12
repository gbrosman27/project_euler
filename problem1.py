# Project Euler - Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(num1, num2):
    # Initialize empty list to hold multiples.
    multiples_list = []

    # Loop through range of numbers from 0-999, adding multiples of 3 and 5 to the list.
    for x in range(0,1000):
        if x % 3 == 0 or x % 5 == 0:
            multiples_list.append(x)
            
    # Use the sum() function to add all numbers in the list.
    return sum(multiples_list)


print(multiples(3,5))