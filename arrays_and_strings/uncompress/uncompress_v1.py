def uncompress(s):
    if len(s) == 0:
        return -1

    number_chars='0123456789'
    output=''
    i=0
    j=0

    while j<len(s):
        if s[j] in number_chars:
            j+=1
        else:
            number=int(s[i:j])
            output+= s[j]*number
            j+=1
            i=j
        
    
    return output

# TODO: Add time and space complexity
"""
def uncompress(s):
    if len(s) == 0:
        return -1
        
    nums_list = '0123456789'
    i = 0
    j = 0
    output = []
    
    while j<len(s):#n
        if s[j] in set(nums_list):#1
            j += 1
        else:
            freq = int(s[i:j])#1
            output.append(freq*s[j])#1
            
            j += 1
            i=j
            
    return ''.join(output)#n

"""
