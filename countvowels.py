def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

s = input("Enter string: ")
print("Vowel count:", count_vowels(s))
