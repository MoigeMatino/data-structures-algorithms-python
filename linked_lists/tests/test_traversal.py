from traversal.traversal_v1 import traverse as traversal_v1, Node
from traversal.traversal_v2 import traverse as traversal_v2


test_case = [
    [ 'a', 'b', 'c', 'd' ],
    [ 'x', 'y' ],
    []
]

def test_traversal_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    assert(traversal_v2(a) == test_case[0])
    assert(traversal_v1(a) == test_case[0])

def test_traversal_x():

    x = Node("x")
    y = Node("y")
    x.next = y

    assert(traversal_v2(x) == test_case[1])
    assert(traversal_v1(x) == test_case[1])

def test_traversal_q():

    q = Node("q")
    assert(traversal_v2(q) == test_case[2])
    assert(traversal_v1(q) == test_case[2])
