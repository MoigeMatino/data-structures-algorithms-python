from is_univalue_list.is_univalue_list_v1 import is_univalue_list 
from traversal.traversal_v1 import Node

test_case = [True, False, True, False, True]

def test_is_univalue_00():
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c
    assert is_univalue_list(a) == test_case[0]

def test_is_univalue_01():
    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c

    assert is_univalue_list(a) == test_case[1]

    