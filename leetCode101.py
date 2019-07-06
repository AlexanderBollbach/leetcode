



	

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


t = TreeNode(1)

tl = TreeNode(2)
tr = TreeNode(2)

tll = None
tlr = TreeNode(3)
trl = None
trr = TreeNode(3)

t.left = tl
t.right = tr

t.left.left = tll 
t.left.right = tlr 

t.right.left = trl
t.right.right = trr


		 #    1
		 #  2   2
		 # n 3 n 3
def preorder(tree):

	if tree == None:
		return [None]

	if tree.left == None and tree.right == None:
		return [tree.val]
	
	vals = [tree.val]

	vals += preorder(tree.left)
	vals += preorder(tree.right)

	return vals


def postorder(tree):

	if tree == None:
		return [None]

	if tree.left == None and tree.right == None:
		return [tree.val]
	
	vals = [tree.val]

	vals += postorder(tree.right)
	vals += postorder(tree.left)
	

	return vals



# class Solution(object):
#     def isSymmetric(self, root):
#         if root == None or root.left == None and root.right == None:
#             return True
#         pre = preorder(root)
#         post = postorder(root)
#         print(pre)
#         print(post)
#         return pre == post
		
# r = Solution().isSymmetric(t)

post = postorder(t)
print(post)
			

		
