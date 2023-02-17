from compress.compress_v1 import compress

test_case = [
    ('ccaaatsss','2c3at3s'),
    ('ssssbbz','4s2bz'),
    ('ppoppppp','2po5p'),
    ('nnneeeeeeeeeeeezz','3n12e2z'),
    ('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy','127y')
]

def test_compress():
    for test in test_case:
        assert compress(test[0])==test[1]
