# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime_numbers(index):
    primes = []

    while len(primes) < index: 
        for num in range(2, index ** 2):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
    
    print(len(primes))    
    print(primes[index])            
    
prime_numbers(1000)