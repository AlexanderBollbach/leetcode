

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



def makeTree(inorder, postorder):
	if len(inorder) == 0 or len(postorder) == 0:
		return None
	i = inorder.index(postorder[-1])

	i1 = inorder[0:i]
	i2 = inorder[i+1:]

	p1 = postorder[0:i]
	p2 = postorder[i:-1]

	t = TreeNode(postorder[-1])
	if len(p1) > 0 and len(i1) > 0:
		t.left = makeTree(i1,p1)
	if len(p2) > 0 and len(i2) > 0:
		t.right = makeTree(i2, p2)
	return t


class Solution(object):
	def test(self, inorder, postorder):
		return makeTree(inorder, postorder)

r = Solution().test([4,2,8,6,9,5,7,1,3], [4,8,9,6,7,5,2,3,1])
printPreorder(r)

