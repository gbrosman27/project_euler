def palindrome():
    i = 100
    pals = []
    while i >= 100 and i <= 999:
        for num in range(100, 1000):
            prod = i * num
            if str(prod) == str(prod)[::-1]:
                pals.append(prod)
        i += 1
    return max(pals)


print(palindrome())