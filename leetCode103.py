
import itertools

def flatten(list1, list2):
	final = []
	for val in itertools.izip_longest(list1, list2, fillvalue=[]):
		final.append(val[0] + val[1])
	return final

def zigZaggify(list):
	final = []
	for i, element in enumerate(list):
		if i % 2 != 0:
			final.append(element[::-1])
		else:
			final.append(element)
	return final



def levelOrder(root):
		if root == None:
			return []
		elif root.left == None and root.right == None:
			return [[root.val]]
		
		left = levelOrder(root.left)
		right = levelOrder(root.right)
		return [[root.val]] + flatten(left, right)

class Solution(object):
	def zigzagLevelOrder(self, root):
		return [e if i % 2 == 0 else e[::-1] for i, e in enumerate(levelOrder(root))]
