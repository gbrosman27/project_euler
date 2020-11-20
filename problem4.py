def palindrome():
    pals = []
    for i in range(100, 1000):
        while i <= 999:
            j = i+1
            answ = i * j
            pals.append(answ)
            i = i + 1
    for num in pals:
        if str(num) == str(num)[::-1]:
            return num

print(palindrome())