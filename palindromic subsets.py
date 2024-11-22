def is_palindrom(s):
    return s==s[::-1]
s="ababa"
palindromic_subsets = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if is_palindrom(s[i:j])]
print(palindromic_subsets)
