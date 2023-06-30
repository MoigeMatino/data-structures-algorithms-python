def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
    key = (i, j)
    if key in memo:
        return memo[key]
    
    if i == len(string_1) or j == len(string_2):
        return 0
    
    if string_1[i] == string_2[j]:
        memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
    else:
        memo[key] = max(
        _overlap_subsequence(string_1, string_2, i + 1, j, memo),
        _overlap_subsequence(string_1, string_2, i, j + 1, memo)
        )
    return memo[key]