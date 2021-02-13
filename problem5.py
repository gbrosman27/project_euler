# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Start at 2 (We know the number will always be divisible by 1)
# Check if number is divisible by i. Return True if no remainder.
def divisible(number):
    for i in range(2,21):
        if number % i != 0:
            return False
    return True


def num_loop():
    # Start the search at 20. We know it will always be even.
    number = 20

    # Loop through the numbers.
    while True:
        if divisible(number):
            break
        number += 20
    return number

print(num_loop())