def find_substrings(words):
    result=[]
    for i in range(len(words)):
        for j in range(len(words)):
            if i!=j and words[i] in words[j]:
                result.append(words[i])
                break
    return result
print(find_substrings(["leetcode", "et","code"]))
