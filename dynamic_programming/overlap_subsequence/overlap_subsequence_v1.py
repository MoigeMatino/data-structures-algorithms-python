def overlap_subsequence(s1:str, s2:str) -> int:
    return _overlap_subsequence(s1, s2, 0, 0)

def _overlap_subsequence(s1:str, s2:str, idx1:int, idx2:int) -> int:
    if idx1 == len(s1) or idx2 == len(s2):
        return 0
    
    if s1[idx1] == s2[idx2]:
        return 1 + _overlap_subsequence(s1, s2, idx1+1, idx2+1)
    else:
        without_s1_prefix = _overlap_subsequence(s1, s2, idx1+1, idx2)
        without_s2_prefix = _overlap_subsequence(s1, s2, idx1, idx2+1)
        return max(without_s1_prefix, without_s2_prefix)
