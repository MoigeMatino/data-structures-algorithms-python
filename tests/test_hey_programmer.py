from hey_programmer.fstring import greet

test_case=[
    ('alvin','hey alvin'),
    ('jason', 'hey jason'),
    ('how now brown cow', 'hey how now brown cow'),
    
]

def test_hey_programmer():
    for test in test_case:
        assert greet(test[0])==test[1]
