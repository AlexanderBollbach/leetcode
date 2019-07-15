# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




def getDepth(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 1
	else:
		lDepth = getDepth(node.left)
		rDepth = getDepth(node.right)
		larger = lDepth if lDepth > rDepth else rDepth
		return larger + 1
	
def isBalanced(tree):
	if tree == None:
		return True

	lDepth = 0
	rDepth = 0
	if tree.left != None:
		lDepth = getDepth(tree.left)
	if tree.right != None:
		rDepth = getDepth(tree.right)

	print('l depth', lDepth)
	print('r depth', rDepth)
	delta = abs(lDepth - rDepth)
	print('delta', delta)
	
	if delta > 1:
		return False
	else:
		l = isBalanced(tree.left)
		r = isBalanced(tree.right)
		return l and r


class Solution(object):
    def isBalanced(self, root):
        return isBalanced(root)
        
