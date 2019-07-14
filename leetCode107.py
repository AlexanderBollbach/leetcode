from itertools import izip_longest as zip_longest


def levelOrder(tree):

	if tree == None:
		return []

	# print(tree.val)
	
	if tree.left == None and tree.right == None:
		return [[tree.val]]
	
	l = levelOrder(tree.left)
	r = levelOrder(tree.right)

	# print(tree.val)
	# print('l:',l)
	# print('r:',r)

	final = []

	for a,b in zip_longest(l[::-1], r[::-1], fillvalue=[]):
		final.append(a + b)

	final.reverse()
	# print(final)
	f = final + [[tree.val]]
	# print(f)

	return f





class Solution(object):
    def levelOrderBottom(self, root):
    	return levelOrder(root)
