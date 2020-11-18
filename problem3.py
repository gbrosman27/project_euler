# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def prime_numbers(num):
    primes = []
    for x in range(2, num+1):
        if num % x == 0:
            primes.append(x)
    return primes



print(prime_numbers(13195))
