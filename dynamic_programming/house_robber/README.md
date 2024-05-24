## **Problem Statement**

A professional robber plans to rob some houses along a street. These houses are arranged in a circle, which means that the first and the last house are neighbors. The robber cannot rob adjacent houses because they have security alarms installed.

Following the constraints mentioned above and given an integer array money representing the amount of money in each house, return the maximum amount the robber can steal without alerting the police.

### **Constraints**:

> 1 ≤ money.length ≤ 10<sup>3</sup>

> 0 ≤ money[ i ] ≤ 10<sup>3</sup>

### **Examples**
    Example 1:
    Input = [1,5,3]           
    Output = 5
    Since 1 and 3 cannot be selected together, the maximum amount to be robbed is 5.

    Example 2:
    Input = [1,2,3,2]           
    Output = 4
    The possible combos are:
    1+3 = 4
    2+2 = 4
    Since both combinations result in 4 and the houses have lower amounts if selected alone, the maximum amount to be robbed is 4.

    Example 3:
    Input = [1,2,10,2]           
    Output = 11
    The possible combinations are:
    1 + 10 = 11
    2 + 2 = 4
    Since 11 is the greatest possible amount, and the houses have lower amounts if selected alone, the maximum amount robbed is 11.



