def compress(s):

    s += '!'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1  
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num)) 
                result.append(s[i])
            i = j
        
    return ''.join(result)

"""
Two pointers technique
Time complexity: O(n)
Space complexity: O(n)

"""
