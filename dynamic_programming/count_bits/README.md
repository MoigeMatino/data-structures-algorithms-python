## **Problem Statement** 

For a given positive integer, n, your task is to return an array of length **n+1** such that for each `x` where `0 ≤ x ≤ n` , `result[x]` is the count of 1s in the binary representation of `x`.

Constraints:

> 0 ≤ n ≤ 10<sup>4</sup>

### **Example**

        Input: n = 3            
        Output = [0,1,1,2]
            x->0: 0  (no ones)
            x->1: 1  (1 one)
            x->2: 10 (1 one)
            x->3: 11 (2 ones)







