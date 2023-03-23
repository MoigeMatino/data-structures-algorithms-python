from intersection.intersection_v1 import intersection as intersection_v1
from intersection.intersection_v2 import intersection as intersection_v2
from intersection.intersection_v3 import intersection as intersection_v3

test_case = [
    (
        [4,2,1,6], [3,6,9,2,10],[6,2]
    ),
    (
        [2,4,6], [4,2], [4,2]
    ),
    (
        [4,2,1], [1,2,4,6], [1,2,4]
    ),
    (
        [0,1,2], [10,11], []
    ),
    (
        [ i for i in range(0, 50000) ], [ i for i in range(0, 50000) ],[i for i in range(0, 50000)]
    )
]

def test_intersection():
    for test in test_case:
        assert intersection_v1(test[0],test[1]) == test[2]
        assert intersection_v2(test[0],test[1]) == test[2]
        assert intersection_v3(test[0],test[1]) == test[2]

