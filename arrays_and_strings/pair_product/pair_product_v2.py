def pair_product_v2(nums, target):
    num_indices = { num: index for index, num in enumerate(nums)}
    
    i = 0
    j = len(nums)-1
    
    nums.sort()
    
    while i < j:
        current_product = nums[i] * nums[j]
        if current_product == target:
            return num_indices[nums[i]], num_indices[nums[j]]
        elif current_product < target:
            i += 1
        else:
            j -= 1
    
    return None

"""
Time complexity: O(nlogn)

The sorting operation takes O(nlogn) time where n is the number of elements in the
input list 'nums'. The subsequent iterations take linear time (O(n)) to find the
pair that adds up to the target value. Therefore, the overall time complexity is
O(nlogn + n) which simplifies to O(nlogn).

Space complexity: O(n)

The space complexity is O(n) because we are using a dictionary to store the indices
of the numbers in the input list 'nums' and this will require at least n entries
in the worst case scenario when all the numbers in the list are unique.

Brain teaser: Why is sorting important in this approach?

"""
