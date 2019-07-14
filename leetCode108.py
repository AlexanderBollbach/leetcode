
def preorder(tree):
    print(tree.val)
    if tree.left:
        preorder(tree.left)
    if tree.right:
        preorder(tree.right)

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def makeTree(nums):
	if len(nums) == 0:
		return None

	i = int(len(nums) / 2)
	t = TreeNode(nums[i])

	if len(nums) == 1:
		return t
	
	f = nums[0:i]
	m = nums[i]
	l = nums[i + 1:]

	if len(f) > 0:
		t.left = makeTree(f)
	if len(l) > 0:
		t.right = makeTree(l)
	return t




class Solution(object):
    def sortedArrayToBST(self, nums):
        return makeTree(nums)
r = Solution().sortedArrayToBST([-5,-3,-1,0,1,3,5])
print(r)
print(preorder(r))
