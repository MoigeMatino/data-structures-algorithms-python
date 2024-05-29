## **Problem Statement** 

You are given a string, `s`, and an array of strings, `word_dict`, representing a dictionary. Your task is to add spaces to `s` to break it up into a sequence of valid words from `word_dict`. We are required to return an array of all possible sequences of words (sentences). The order in which the sentences are listed is not significant.

> Note: The same dictionary word may be reused multiple times in the segmentation.

Constraints:

    1 ≤ s.length ≤ 20

    1 ≤ word_dict.length ≤ 1000

    1 ≤ word_dict[i].length ≤ 10

    s and word_dict[i] consist of only lowercase English letters.

    All the strings of word_dict are unique.

### **Example**

    s = "catsanddogs"
    word_dict = ["cat", "and", "cats", "sand", "dog"]

    Output: ["cats and dog", "cat sand dog"]
