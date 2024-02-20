from collections import Counter

def most_frequent_char(s):
    tracker = Counter(s)
    most_frequent_char = None
    for char in s:
        if most_frequent_char is None or tracker[char] > tracker[most_frequent_char]:
            most_frequent_char = char
    return most_frequent_char
