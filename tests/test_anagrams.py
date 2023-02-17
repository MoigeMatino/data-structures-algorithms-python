import pytest
from structy.

test_case=[
    ('restful', 'fluster'),
    ('cats', 'tocs'),
    ('monkeyswrite', 'newyorktimes'),
    ('paper', 'reapa')
]
@pytest.fixture
def example_anagram_data():
    return [

        ('paper', 'reapa')
        ('restful', 'fluster'),
        ('cats', 'tocs'),
        ('monkeyswrite', 'newyorktimes'),

    ]

def test_anagrams():
    assert anagrams(example_anagram_data)
