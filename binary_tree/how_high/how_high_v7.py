def how_high(root):
	if root is None:
		return -1
		
	stack = [(root,0)]
	max_height = float("-inf")
	
	while stack:
		current, current_height = stack.pop()
		
		if current.left is None and current.right is None:
			if current_height > max_height:
				max_height = current_height
		
		if current.right:
			stack.append((current.right, current_height+1))
		
		if current.left:
			stack.append((current.left, current_height+1))
			
	return max_height