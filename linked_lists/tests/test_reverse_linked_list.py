from reverse_linked_list.reverse_linked_list_v1 import reverse_list as reverse_list_v1
from traversal.traversal_v1 import Node

test_case = ['f','y','p']

def test_reverse_linked_list_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    assert reverse_list_v1(a) == test_case[0]

def test_reverse_linked_list_x():
    x = Node("x")
    y = Node("y")

    x.next = y

    assert reverse_list_v1(x) == test_case[1]

def test_reverse_linked_list_p():
    p = Node("p")

    assert reverse_list_v1(p) == test_case[2]
    