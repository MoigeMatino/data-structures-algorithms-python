from typing import Dict, Tuple

def count_palindromic_substrings(s: str) -> int:
    total_palindromes = 0
    memo = {}

    for start in range(len(s)):
        for end in range(start, len(s)):
            if is_palindrome(s, start, end, memo):
                total_palindromes += 1
    
    return total_palindromes

def is_palindrome(s:str, start:int, end:int, memo: Dict[Tuple[int, int], bool]) -> bool:
    key = start, end
    if key in memo:
        return memo[key]
    
    if start == end:
        return True
    
    if start > end:
        return False
    
    if s[start] == s[end]:
        if end - start == 1 or is_palindrome(s, start+1, end-1, memo):
            memo[key] = True
            return True
        
    memo[key] = False  
    return False