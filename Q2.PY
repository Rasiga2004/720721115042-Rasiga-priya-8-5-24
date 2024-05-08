def longest_common_prefix(strs):
    if not strs:
        return ""
    
    
    strs.sort()
    
    
    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break
    
    return prefix


strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  
