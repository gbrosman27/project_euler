# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome():
    # Initialize counter for i.
    i = 100

    # Set empty list for palindrome numbers.
    pals = []

    # Multiply all the numbers in the range of 100-999 by i.
    while i >= 100 and i <= 999:
        for num in range(100, 1000):
            prod = i * num

            # If the current product is a palindrome, add it to the list.
            if str(prod) == str(prod)[::-1]:
                pals.append(prod)

        # Increment i by 1 and multiply by the nums in range again.
        i += 1

    # Return the max palindrome from the list.
    return max(pals)


print(palindrome())