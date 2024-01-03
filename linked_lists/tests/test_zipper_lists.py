from traversal.traversal_v1 import Node
from zipper_lists.zipper_lists_v1 import zipper_lists as zipper_lists_v1
from zipper_lists.zipper_lists_v2 import zipper_lists as zipper_lists_v2

test_case = [
    'a', 's', 'w', 1
]


def test_zipper_lists_a_x():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    zipper_list_head_v1 = zipper_lists_v1(a, x) 
    assert zipper_list_head_v1.val == test_case[0]
    assert zipper_list_head_v1.next.val == 'x'

    zipper_list_head_v2 = zipper_lists_v2(a, x) 
    assert zipper_list_head_v2.val == test_case[0]
    assert zipper_list_head_v2.next.val == 'x'

def test_zipper_lists_s_one():
    s = Node("s")
    t = Node("t")
    s.next = t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four

    zipper_list_head_v1 = zipper_lists_v1(s, one) 
    assert zipper_list_head_v1.val == test_case[1]
    assert zipper_list_head_v1.next.val == 1
    assert zipper_list_head_v1.next.next.val == 't'

    zipper_list_head_v2 = zipper_lists_v2(s, one) 
    assert zipper_list_head_v2.val == test_case[1]
    assert zipper_list_head_v2.next.val == 1
    

