# using the Counter from the collections module
# we can count the occurrences of each character in a string.

from collections import Counter

def anagrams(s1, s2):
    s1_dict = Counter(s1)
    s2_dict = Counter(s2)
    return s1_dict == s2_dict

"""
n - number of elements in s1
m - number of elements in s2

Time Complexity: O(n+m)

Constructing these counters involves iterating 
through each character in each string, resulting 
in a time complexity of O(n + m), where n, m is the length 
strings s1 and s2 respectively.

Space complexity: O(n+m)

The space complexity of this solution is also O(n+m). We are
storing two dictionaries (or Counter objects), one for each input string. 
The size of these dictionaries depends on the number of unique characters 
in their respective strings. In the worst case scenario, if all characters 
in both strings are unique, then the space complexity would
be O(n*m), but since usually there will be common characters between
the two strings, the actual space complexity will be less than that.

"""