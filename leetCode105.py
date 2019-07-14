

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def printPreorder(root): 
	if root: 
		print(root.val)
		printPreorder(root.left) 
		printPreorder(root.right) 



def makeTree(preorder, inorder):
	if len(preorder) == 0 or len(inorder) == 0:
		return None
	i = inorder.index(preorder[0])
	p1 = preorder[1:i+1]
	p2 = preorder[i+1:]
	i1 = inorder[0:i]
	i2 = inorder[i+1:]
	t = TreeNode(preorder[0])
	if len(p1) > 0 and len(i1) > 0:
		t.left = makeTree(p1, i1)
	if len(p2) > 0 and len(i2) > 0:
		t.right = makeTree(p2, i2)
	return t


class Solution(object):
	def test(self, preorder, inorder):
		return makeTree(preorder, inorder)

r = Solution().test([3,9,20,15,7], [9,3,15,20,7])
printPreorder(r)

