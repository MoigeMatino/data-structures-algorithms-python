from max_value.max_value_v1 import max_value
from max_value.max_value_v2 import max_value as max_value2
test_case = [

    ([4, 7, 2, 8, 10, 9],10),
    ([10, 5, 40, 40.3],40.3),
    ([-5, -2, -1, -11],-1),
    ([42],42),
    ([1000, 8],1000),
    ([1000, 8, 9000],9000),
    ([2, 5, 1, 1, 4],5),
    
]

def test_max_value():
    for test in test_case:
        assert max_value(test[0])==test[1]
        assert max_value2(test[0])==test[1]