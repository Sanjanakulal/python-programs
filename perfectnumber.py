def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

n = int(input("Enter number: "))
print("Perfect number" if is_perfect(n) else "Not perfect")
