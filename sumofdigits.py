def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(n))
