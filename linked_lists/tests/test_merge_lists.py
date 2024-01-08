from merge_lists.merge_lists_v1 import merge_lists as merge_lists_v1
from merge_lists.merge_lists_v2 import merge_lists as merge_lists_v2
from traversal.traversal_v1 import Node

test_case = [
    5,
    1,
    15
]

def test_merge_lists_5_6():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    
    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t

    merge_lists_head_v1 = merge_lists_v1(a, q)
    assert merge_lists_head_v1.val == test_case[0]
    assert merge_lists_head_v1.next.val == 6

def test_merge_lists_5_1():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t

    merge_lists_head_v1 = merge_lists_v1(a, q)
    assert merge_lists_head_v1.val == test_case[1]
    assert merge_lists_head_v1.next.val == 5

def test_merge_lists_30_15():
    h = Node(30)

    p = Node(15)
    q = Node(67)
    p.next = q

    merge_lists_head_v1 = merge_lists_v1(h, p)
    assert merge_lists_head_v1.val == test_case[2]
    assert merge_lists_head_v1.next.val == 30