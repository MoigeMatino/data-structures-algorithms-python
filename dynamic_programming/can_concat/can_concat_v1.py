def can_concatenate(s:str, words:list[str]) -> bool:
    if len(s) == 0:
        return True
        
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if can_concatenate(suffix, words) == True:
                return True
                
    return False