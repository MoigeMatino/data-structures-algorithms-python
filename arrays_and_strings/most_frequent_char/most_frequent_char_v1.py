def most_frequent_char(s):
    tracker = {}
    for char in s:
        if char in tracker:
            tracker[char] +=1
        tracker[char] = 1

    proxy=None
    for char in s:
        if not proxy or tracker[char] > tracker[proxy]:
            proxy=char

    return proxy

"""

    n = length of string
    Time: O(n)
    Space: O(n)

"""