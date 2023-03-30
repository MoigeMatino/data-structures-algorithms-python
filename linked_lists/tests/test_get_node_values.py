from get_node_value.get_node_value_v1 import get_node_value as get_node_value_v1
from get_node_value.get_node_value_v2 import get_node_value as get_node_value_v2
from traversal.traversal_v1 import Node

test_case = [
    'c', 'd', None, 'banana', 'mango'
]

def test_get_node_value_c():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d
    assert get_node_value_v1(a, 2) == test_case[0]
    assert get_node_value_v2(a, 2) == test_case[0]

def test_get_node_value_d():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d
    assert get_node_value_v1(a, 3) == test_case[1]
    assert get_node_value_v2(a, 3) == test_case[1]

def test_get_node_value_none():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d
    assert get_node_value_v1(a, 7) == test_case[2]
    assert get_node_value_v2(a, 7) == test_case[2]

def test_get_node_value_banana():
    node1 = Node("banana")
    node2 = Node("mango")

    node1.next = node2
    assert get_node_value_v1(node1, 0) == test_case[3]
    assert get_node_value_v2(node1, 0) == test_case[3]

def test_get_node_value_mango():
    node1 = Node("banana")
    node2 = Node("mango")

    node1.next = node2
    assert get_node_value_v1(node1, 1) == test_case[4]
    assert get_node_value_v2(node1, 1) == test_case[4]