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