def count_map(s):
    count_dict={}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char]=1

    return count_dict

def anagrams(s1,s2):
    return count_map(s1) == count_map(s2)

"""
n = length of string 1
m = length of string 2

Time: O(n + m)
Space: O(n + m)

"""