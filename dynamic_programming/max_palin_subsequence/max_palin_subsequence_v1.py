def max_palin_subsequence(s):
    end = len(s)-1
    return _max_palin_subsequence(s, 0, end)

def _max_palin_subsequence(s, start, end):
    if start == end:
        return 1
    
    if start > end:
        return 0
    
    if s[start] == s[end]:
        return 2 + _max_palin_subsequence(s, start+1, end-1)
    else:
        new_first = _max_palin_subsequence(s, start+1, end)
        new_last = _max_palin_subsequence(s, start, end-1)
        return max(new_first, new_last)
    