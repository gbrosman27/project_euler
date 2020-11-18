# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def prime_numbers(num):
    # Set initial value of where to start the iterations at 2.
    i = 2

    # Create an empty list to hold prime numbers.
    primes = []

    # while each iteration is less than or equal to the passed in number...
    while i <= num:

        # If the passed in number divided by the current iteration has a remainder of 0...
        if num % i == 0:

            # Add that number to the list as it is prime.
            primes.append(i)

            # Set the num equal to the passed in num divided by the current iteration.
            # This will provide prime factors, not all prime numbers.
            num = num / i
        else: 

            # Set i equal to the current iteration + 1 to move the iteration forward.
            i = i + 1

    return primes



print(prime_numbers(600851475143))
