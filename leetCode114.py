def flatten(tree):
	if not tree:
		return
	if tree.left:
		flatten(tree.left)
	if tree.right:
		flatten(tree.right)

	r = tree.right
	tree.right = tree.left
	temp = tree
	tree.left = None

	while temp and temp.right:
		temp = temp.right

	if temp:
		temp.right = r
	
	
    
class Solution(object):
    def flatten(self, root):
        flatten(root)
