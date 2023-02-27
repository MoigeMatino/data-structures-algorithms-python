def most_frequent_char(s):
    tracker = {}
    for char in s:
        if char in tracker:
            tracker[char] += 1
        else:
            tracker[char] = 1
    return max(tracker,key=tracker.get)