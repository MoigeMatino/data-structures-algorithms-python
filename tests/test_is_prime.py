from is_prime.is_prime import is_prime

test_case = [
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (6,False),
    (7,True),
    (8,False),
    (25,False),
    (31,True),
    (2017,True),
    (2048,False),
    (1,False),
    (713,False),
]

def test_is_prime():
    for test in test_case:
        assert is_prime(test[0])==test[1]
