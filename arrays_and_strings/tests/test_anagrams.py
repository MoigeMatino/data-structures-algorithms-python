from anagrams import anagrams_v1 as anagrams

test_case=[
        ('paper', 'reapa',False),
        ('restful', 'fluster',True),
        ('cats', 'tocs',False),
        ('monkeyswrite', 'newyorktimes',True),
        ('elbow', 'below', True),
        ('tax', 'taxi',False),
        ('taxi', 'tax', False),
        ('night', 'thing', True),
        ('abbc', 'aabc', False),
        ('po', 'popp', False),
        ('pp', 'oo',False)

]

def test_anagrams():
    for item in test_case:
        assert anagrams.anagrams(item[0],item[1]) == item[2]
