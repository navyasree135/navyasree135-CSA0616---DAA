s="babad"
print(max((s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i:j]==s[i:j][::-1]),key=len))

