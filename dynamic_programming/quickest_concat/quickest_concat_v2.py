def quickest_concat(s, words):
    result = _quickest_concat(s, words, {})
    if result == float('inf'):
        return -1
    else:
        return result

def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]
    
    if s == '':
        return 0
    
    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            attempt = 1 + _quickest_concat(suffix, words, memo)
            min_words = min(attempt, min_words)
    
    memo[s] = min_words
    return min_words

"""

s = length of string
w = # of words
Time: ~O(sw)
Space: O(s)

"""