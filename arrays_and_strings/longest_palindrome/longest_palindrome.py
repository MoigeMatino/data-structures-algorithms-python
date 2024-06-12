from collections import defaultdict

def longest_palindrome(s:str) -> int:
    count_map = defaultdict(int)
    has_odd_count = False
    max_palindrome = 0

    for char in s:
        count_map[char] += 1

    if len(count_map) == 1:
        for char in count_map:
            return count_map[char]
    
    for count in count_map.values():
        if count % 2 == 1:
            has_odd_count = True
        max_palindrome += (count // 2) * 2

    if has_odd_count:
        max_palindrome += 1

    return max_palindrome
