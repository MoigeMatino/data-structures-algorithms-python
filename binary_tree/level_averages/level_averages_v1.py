from collections import deque
from statistics import mean

def level_averages(root):
    if root is None:
        return []
    
    queue = deque([(root,0)])
    level_averages = []  
    avgs = []
    
    while queue:
        current, level = queue.popleft()
        
        if len(level_averages) == level:
            level_averages.append([current.val])
        else:
            level_averages[level].append(current.val)
        
        if current.left:
            queue.append((current.left, level+1))

        if current.right:
            queue.append((current.right, level+1))
            
        
    for level in level_averages:
        avgs.append(mean(level))
    
    return avgs