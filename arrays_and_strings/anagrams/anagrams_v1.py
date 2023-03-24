def count_map(s):
    count={}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char]=1

    return count

def anagrams(s1,s2):
    return count_map(s1) == count_map(s2)