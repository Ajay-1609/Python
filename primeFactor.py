print("Enter a number:")
num = int(__import__("builtins").input())

if num <= 1:
    print("Please enter a number greater than 1.")
else:
    prime_factors = []

    # Check for factor 2
    if num % 2 == 0:
        prime_factors.append(2)
        while num % 2 == 0:
            num = num // 2

    # Check for odd factors
    i = 3
    while i * i <= num:
        if num % i == 0:
            # Avoid duplicates manually
            if i not in prime_factors:
                prime_factors.append(i)
            while num % i == 0:
                num = num // i
        i += 2

    # If num is still a prime greater than 2
    if num > 2:
        if num not in prime_factors:
            prime_factors.append(num)

    print("Distinct prime factors:")
    for factor in prime_factors:
        print(factor, end=' ')