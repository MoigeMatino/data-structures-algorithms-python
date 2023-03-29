from linked_list_find.linked_list_find_v1 import linked_list_find as linked_list_find_v1 
from linked_list_find.linked_list_find_v2 import linked_list_find as linked_list_find_v2
from traversal.traversal_v1 import Node

test_case = [True, True, False, True, True, False]

def test_linked_list_find_c():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    assert linked_list_find_v1(a,"c") == test_case[0]
    assert linked_list_find_v2(a,"c")==test_case[0]
    

def test_linked_list_find_d():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    assert linked_list_find_v1(a,"d")==test_case[1]
    assert linked_list_find_v2(a,"d")==test_case[1]


def test_linked_list_find_q():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    assert linked_list_find_v1(a,"q")==test_case[2]
    assert linked_list_find_v2(a,"q")==test_case[2]

    
def test_linked_list_find_jason():
    node1 = Node("jason")
    node2 = Node("leneli")

    node1.next = node2

    assert linked_list_find_v1(node1,"jason")==test_case[3]
    assert linked_list_find_v2(node1,"jason")==test_case[3]


def test_linked_list_find_42():
    node1 = Node(42)
    assert linked_list_find_v1(node1,42)==test_case[4]
    assert linked_list_find_v2(node1,42)==test_case[4]
    

def test_linked_list_find_100():
    node1 = Node(42)
    assert linked_list_find_v1(node1,100)==test_case[5]
    assert linked_list_find_v2(node1,100)==test_case[5]
