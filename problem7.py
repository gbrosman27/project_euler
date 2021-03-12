# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime_numbers():  
    primes = []

    # while each iteration is less than or equal to the passed in number...
    for num in range(2, ):
        if num > 1:
            for i in range(2, num):

                # If the passed in number divided by the current iteration has a remainder of 0...
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print(primes)
                           
                
    
prime_numbers()