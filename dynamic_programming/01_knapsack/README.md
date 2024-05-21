## **Problem Statement** 

You are given `n` items whose weights and values are known, as well as a knapsack to carry these items. The knapsack cannot carry more than a certain maximum weight, known as its `capacity`.

You need to maximize the total value of the items in your knapsack, while ensuring that the sum of the weights of the selected items does not exceed the capacity of the knapsack.

If there is no combination of weights whose sum is within the capacity constraint, return 0.

> 

    Notes:

        An item may not be broken up to fit into the knapsack, i.e.,
        an item either goes into the knapsack in its entirety or not at all.
        We may not add an item more than once to the knapsack.

Constraints:

    1 ≤ capacity ≤ 1000
    1 ≤ values.length ≤ 500
    weights.length == values.length
    1 ≤ values[i] ≤ 1000
    1 ≤ weights[i] ≤ capacity

### **Example**

    capacity = 30
    weights = [10,20,30]
    values = [22,33,44]

    Output = 55
    Using weights 20 and 10 to reach max capacity with values of 22 and 33 to give us max profit of 55
    Using the weight of 30 would give us a max profit of 44




