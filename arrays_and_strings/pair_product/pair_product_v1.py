def pair_product(numbers, target_product):
    nums_dict={}
    for index, num in enumerate(numbers):
        quotient=target_product/num
        if quotient in nums_dict:
            return nums_dict[quotient], index
        nums_dict[num]=index

"""
n = number of elements in the list
Time complexity: O(n)
Space complexity: O(n)
"""