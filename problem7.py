# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime_num(index):
    # Find prime numbers. use generator. find index 10001.
    primes_list = []
    for num in range(2, index):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes_list.append(num)
    print(len(primes_list))
                    




prime_num(10001)