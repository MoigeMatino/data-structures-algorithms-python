def pair_product(numbers, target_product):
    nums_dict={}
    for index, num in enumerate(numbers):
        if quotient:=target_product/num in nums_dict and nums_dict[quotient] != index:
            return index,nums_dict[quotient]
        nums_dict[num]=index

"""
n = number of elements in the list
Time complexity: O(n)
Space complexity: O(n)
"""