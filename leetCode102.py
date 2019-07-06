class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import itertools

def flatten(list1, list2):
	final = []
	for val in itertools.izip_longest(list1, list2, fillvalue=[]):
		final.append(val[0] + val[1])
	return final


class Solution(object):
	def levelOrder(self, root):
		if root == None:
			return [[]]
		elif root.left == None and root.right == None:
			return [[root.val]]
		
		left = self.levelOrder(root.left)
		right = self.levelOrder(root.right)
		return [[root.val]] + flatten(left, right)
		

t = TreeNode(3)
tl = TreeNode(9)
tr = TreeNode(20)
trl = TreeNode(15)
trr = TreeNode(7)
t.left = tl
t.right = tr
tr.left = trl
tr.right = trr

r = Solution().levelOrder(t)
assert(r == [[3],[9,20],[15,7]])
