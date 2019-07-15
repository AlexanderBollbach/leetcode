# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def getLinkedListLength(node):
	count = 1
	
	while node.next != None:
		count += 1
		node = node.next
		
	return count 


def getMidNode(node):
	l = getLinkedListLength(node)
	m = int(l / 2)	
	m = m - 1

	if l == 1:
		m = 0
	if l == 2:
		m = 0
	if l == 3:
		m = 0


	print('mid index ', m)

	count = 0
	
	while count < m:
		node = node.next
		count += 1
	
	return node



def listToTree(node):

	if node == None:
		return None

	if node.next == None:
		print('return leaf ', node.val)
		return TreeNode(node.val)
	
	m = getMidNode(node)
	root = m.next
	
	# print('m ', m.val)
	# print('root ', root.val)

	t = TreeNode(root.val)

	m.next = None

	if root.next != None:
		t.right = listToTree(root.next)
	t.left = listToTree(node)
	return t



class Solution(object):
    def sortedListToBST(self, head):
        return listToTree(head)
        
