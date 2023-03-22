from pair_product.pair_product_v1 import pair_product

test_case = [
    ([3, 2, 5, 4, 1], 8,(1,3)),
    ([3, 2, 5, 4, 1], 10,(1,2)),
    ([4, 7, 9, 2, 5, 1], 5,(4,5)),
    ([4, 7, 9, 2, 5, 1], 35,(1,4)),
    ([3, 2, 5, 4, 1], 10,(1,2)),
]

def test_pair_product():
    for test in test_case:
        assert pair_product(test[0],test[1])==test[2]