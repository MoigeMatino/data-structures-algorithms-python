def tree_levels(root):
    levels = []
    _tree_levels(root, levels, 0)
    return levels


def _tree_levels(root, levels, level_num):
    if root is None:
        return
    
    if level_num == len(levels):
        levels.append([ root.val ])
    else:
        levels[level_num].append(root.val)
    
    _tree_levels(root.left, levels, level_num + 1)
    _tree_levels(root.right, levels, level_num + 1)  

"""
DFS recursive approach

n = number of nodes
Time: O(n)
Space: O(n)

"""
    
