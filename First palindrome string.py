strings = ["apple", "level", "banana", "radar"]

for s in strings:
    if s == s[::-1]:  # Check if the string is a palindrome
        print("First palindrome string:", s)
        break
else:
    print("No palindrome found")
