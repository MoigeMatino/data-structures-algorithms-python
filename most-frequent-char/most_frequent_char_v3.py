def most_frequent_char(s):
    tracker = {}
    for char in s:
        if char in tracker:
            tracker[char] += 1
        else:
            tracker[char] = 1
    return max(tracker,key=tracker.get)

"""
the return expression finds the key with the maximum value
Another way to find the key with the maximum value:
- max(tracker, key=lambda x:tracker[x])
"""