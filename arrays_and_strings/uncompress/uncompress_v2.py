def uncompress(s):
    if len(s) == 0:
        return -1
        
    nums_list = '0123456789'
    i = 0
    j = 0
    output = []
    
    while j<len(s):
        if s[j] in set(nums_list):
            j += 1
        else:
            freq = int(s[i:j])
            output.append(freq*s[j])
            
            j += 1
            i=j
            
    return ''.join(output)