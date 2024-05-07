from typing import Union
def quickest_concat(s:str, words:list[str]) -> int:
    result = _quickest_concat(s, words)
    if result == float('inf'):
        return -1
    return result

def _quickest_concat(s:str, words:list[str]) -> Union[float,int]:
    if len(s) == 0:
        return 0
    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            num_words = 1 + _quickest_concat(suffix, words)
            min_words = min(num_words, min_words)
            
    return min_words            