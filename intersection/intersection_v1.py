def intersection(a,b):
    intersection=[]
    my_set={element for element in a}
    for element in b:
        if element in my_set:
            intersection.append(element)
    return intersection

