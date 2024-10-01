## **Problem Statement**

Given the root of a binary tree, return the maximum sum of any non-empty path.

A path in a binary tree is defined as follows:

        A sequence of nodes in which each pair of adjacent nodes must have an edge connecting them.
        A node can only be included in a path once at most.
        Including the root in the path is not compulsory.

You can calculate the path sum by adding up all node values in the path. To solve this problem, calculate the maximum path sum given the root of a binary tree so that there won’t be any greater path than it in the tree.


### Constraints

> 1 ≤ Number of nodes in the tree ≤ 500.

> −1000 ≤ Node.value ≤ 1000