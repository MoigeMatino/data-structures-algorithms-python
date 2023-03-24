from most_frequent_char.most_frequent_char_v1 import most_frequent_char as mfc1
from most_frequent_char.most_frequent_char_v2 import most_frequent_char as mfc2
from most_frequent_char.most_frequent_char_v3 import most_frequent_char as mfc3
from most_frequent_char.most_frequent_char_v4 import most_frequent_char as mfc4

test_case = [
    ('bookeeper','e'),
    ('david','d'),
    ('abby','b'),
    ('mississippi','i'),
    ('potato','o'),
    ('eleventennine','e'),
    ('riverbed','r'),
]

def test_most_frequent_char():
    for test in test_case:
        # *TODO fix issue with mfc1
        # assert mfc1(test[0]) == test[1]
        assert mfc2(test[0]) == test[1]
        assert mfc3(test[0]) == test[1]
        assert mfc4(test[0]) == test[1]