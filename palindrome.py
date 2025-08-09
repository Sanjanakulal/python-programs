def is_palindrome(s):
    return s == s[::-1]

s = input("Enter string: ")
print("Palindrome" if is_palindrome(s) else "Not palindrome")
