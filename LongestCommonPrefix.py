ls = ['google', 'googly', 'goose', 'goosebumps', 'googol', 'googly', 'goofball']

def longestCommonPrefix(ls):
    
    common = ''

    first = min(ls)
    last = max(ls)

    for i, c in zip(first, last):
        if i == c:
            common += i
        else:
            break
    

    return common

print(longestCommonPrefix(ls))