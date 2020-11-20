def palindrome():
    pals = [item * item+1 for item in range(10,200)]
    for num in pals:
        if str(num) == str(num)[::-1]:
            print(num)
    

print(palindrome())