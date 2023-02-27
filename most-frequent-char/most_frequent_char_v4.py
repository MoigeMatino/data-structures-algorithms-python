from collections import Counter

def most_frequent_char(s):
    tracker = Counter(s)
    proxy = None
    for char in s:
        if proxy is None or tracker[char] > tracker[proxy]:
            proxy = char
    return proxy