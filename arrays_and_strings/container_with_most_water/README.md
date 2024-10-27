## **Problem Statement**

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Example 1
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
    In this case, the max area of water the container can contain is 49. Derived from (1, height[1]) and (8, height[8]) which gives us the heights; h1 = 8, h2 = 7. 
    To get the width: 8 - 1 = 7
    To get height = min(8, 7) = 7
    To get area = height * width = 7 * 7 = 49

### Example 2
    Input: height = [1,1]
    Output: 1