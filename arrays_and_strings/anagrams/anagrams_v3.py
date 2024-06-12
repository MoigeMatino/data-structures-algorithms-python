from collections import defaultdict
from typing import Dict

def anagrams(s1:str, s2:str) -> bool:
    s1_counter = build_dict(s1)
    s2_counter = build_dict(s2)

    return s1_counter == s2_counter

def build_dict(s:str) -> Dict:
    s_dict = defaultdict(int)

    for char in s:
        s_dict[char] += 1
    
    return s_dict   
