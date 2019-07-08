def max(a, b):
	return a if a > b else b

def getDepth(tree):
	if tree == None:
		return 0
	left = getDepth(tree.left)
	right = getDepth(tree.right) 
	return max(left,right) + 1


class Solution(object):
	def maxDepth(self, root):
		return getDepth(root)
