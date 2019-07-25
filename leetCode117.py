class Node(object):
	def __init__(self, val, left, right, next):
		self.val = val
		self.left = left
		self.right = right
		self.next = next


def preorder(tree):
	print(tree.val, end=' ')
	if tree.left:
		preorder(tree.left)
	if tree.right:
		preorder(tree.right)

def inorder(tree):
	
	if tree.left:
		inorder(tree.left)
	print(tree.val, end=' ')
	if tree.right:
		inorder(tree.right)





# def connect(left, right):

# 	# if left:
# 	# 	print(left.val)
# 	# else:
# 	# 	print('left: null')
# 	# if right:
# 	# 	print(right.val)
# 	# else:
# 	# 	print('right: null')

# 	if left:
# 		connect(left.left, left.right)
# 	if right:
# 		connect(right.left, right.right)

# 	if left and right:
# 		temp = left
# 		while temp.next:
# 			temp = temp.next
# 			if temp == right:
# 				break
# 		if temp != right:
# 			# print('join')
# 			# print(temp.val)
# 			# print(right.val)
# 			temp.next = right


		
		

# 		if left.right and right.left:
# 			connect(left.right, right.left)
# 		if left.right and right.right:
# 			connect(left.right, right.right)
# 		if left.left and right.left:
# 			connect(left.left, right.left)
# 		if left.left and right.right:
# 			connect(left.left, right.right)
	


def connect(tree):
	
	curr = tree
	nextFirst = tree

	while True:
		assignedNextFirst = False
		curr = nextFirst
		tracker = None

		print('====: starting at', curr.val)
		
		while True:
			next = curr.next

			if curr.left and curr.right:
				curr.left.next = curr.right
				if tracker:
					tracker.next = curr.left
				tracker = curr.right
				print('assigned ', curr.left.val, curr.right.val)
			if curr.left and not curr.right:
				if tracker:
					print('assigned ', tracker.val, curr.left.val)	
					tracker.next = curr.left
				tracker = curr.left
				print('started tracker ', tracker.val)	
			elif curr.right and not curr.left:
				if tracker:
					print('assigned ', tracker.val, curr.right.val)
					tracker.next = curr.right
				tracker = curr.right
				print('started tracker ', tracker.val)
					
			if not assignedNextFirst:
				if curr.left:
					nextFirst = curr.left
					assignedNextFirst = True
					# print('next first is ', curr.left.val)
				elif curr.right:
					nextFirst = curr.right
					assignedNextFirst = True
					# print('next first is ', curr.right.val)

			curr = next

			if not next:
				# print('======= end of level ', curr.val)
				break

			

		# print('assignedNextFirst after: ', assignedNextFirst)

		if not assignedNextFirst:
			break

		



class Solution(object):
	def connect(self, root):
		if root:
			connect(root)
		return root
			

t = Node(1,None,None,None)

l = Node(2,None,None,None)
l.left = Node(4,None,None,None)
# l.right = Node(5,None,None,None)

r = Node(3,None,None,None)
# r.left = Node(6,None,None,None)
r.right = Node(7,None,None,None)

lll = Node(8,None,None,None)
llr = Node(9,None,None,None)

lrl = Node(10,None,None,None)
lrr = Node(11,None,None,None)

rll = Node(12,None,None,None)
rlr = Node(13,None,None,None)

rrl = Node(14,None,None,None)
rrr = Node(15,None,None,None)

# l.left.left = lll 
# l.left.right = llr 

# l.right.left = lrl 
# l.right.right = lrr 

# r.left.left = rll 
# r.left.right = rlr

# r.right.left = rrl
# r.right.right = rrr

t.left = l
t.right = r

print('--algo--')
result = Solution().connect(t)

# preorder(t)
# print('\n')
# inorder(t)
# print('\n')


