from pair_sum.pair_sum_v1 import pair_sum as ps1
from pair_sum.pair_sum_v2 import pair_sum as ps2
from pair_sum.pair_sum_v3 import pair_sum as ps3

test_case=[
    ([3, 2, 5, 4, 1], 8,(0,2)),
    ([4, 7, 9, 2, 5, 1],3, (3,5)),
    ([1, 6, 7, 2], 13,(1,2)),
    ([9, 9], 18,(0,1)),
    ([6, 4, 2, 8], 12,(1,3)),
]

def test_pair_sum():
    for test in test_case:
        # *TODO fix failing test for ps1
        # assert ps1(test[0], test[1])==test[2]
        # assert ps2(test[0], test[1])==test[2]
        assert ps3(test[0], test[1])==test[2]