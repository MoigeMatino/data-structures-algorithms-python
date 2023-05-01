from statistics import mean

def level_averages(root):
    levels = []
    fill_levels(root, levels, 0)
    
    avgs = []
    for level in levels:
        avgs.append(mean(level))
    return avgs
        
def fill_levels(root, levels, level_num):
    if root is None:
        return
    
    if level_num == len(levels):
        levels.append([ root.val ])
    else:
        levels[level_num].append(root.val)
    
    fill_levels(root.left, levels, level_num + 1)
    fill_levels(root.right, levels, level_num + 1)

"""
DFS recursive approach

n = number of nodes
Time: O(n)
Space: O(n)

"""