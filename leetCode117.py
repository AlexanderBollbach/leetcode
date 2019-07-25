class Node(object):
	def __init__(self, val, left, right, next):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

def connect(tree):	
	nextFirst = tree

	while True:
		assignedNextFirst = False
		curr = nextFirst
		tracker = None

		while True:
			next = curr.next

			if curr.left and curr.right:
				curr.left.next = curr.right
				if tracker:
					tracker.next = curr.left
				tracker = curr.right
			if curr.left and not curr.right:
				if tracker:
					tracker.next = curr.left
				tracker = curr.left
			elif curr.right and not curr.left:
				if tracker:
					tracker.next = curr.right
				tracker = curr.right
					
			if not assignedNextFirst:
				if curr.left:
					nextFirst = curr.left
					assignedNextFirst = True
				elif curr.right:
					nextFirst = curr.right
					assignedNextFirst = True

			curr = next

			if not next:
				break
				
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


