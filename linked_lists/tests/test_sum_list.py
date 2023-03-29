from sum_list.sum_list_v1 import sum_list as sum_list_v1
from sum_list.sum_list_v2 import sum_list as sum_list_v2
from traversal.traversal_v1 import Node

test_case = [19, 42, 100, 0]

def test_sum_list_a():
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert sum_list_v1(a)==test_case[0]
    assert sum_list_v2(a)==test_case[0]

def test_sum_list_x():
    x = Node(38)
    y = Node(4)

    x.next = y

    assert sum_list_v1(x)==test_case[1]
    assert sum_list_v2(x)==test_case[1]

def test_sum_list_z():
    z = Node(100)
    assert sum_list_v1(z)==test_case[2]
    assert sum_list_v2(z)==test_case[2]

def test_sum_list_none():
    assert sum_list_v1(None)==test_case[3]
    assert sum_list_v2(None)==test_case[3]
