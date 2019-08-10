class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# helper: once we know we are in the cycle we can loop around it once and see if some other is inside the cycle.  
# this helps to find the first node in the cycle by incrementally inches up on it from the start
def cycle_and_find(head, other):
  temp = head
  while temp and temp.next:
    temp = temp.next
    if temp == other:
      return True
    if temp == head:
      return False
  return False

def findACycleNode(head):
  slow = head
  fast = head.next 
  loop_node = None
  while slow.next and fast.next and fast.next.next:
    if slow == fast:
      return slow
    slow = slow.next 
    fast = fast.next.next

def run(head):

  if not head or not head.next:
    return False 

  # find any node in the cycle
  cycle_node = findACycleNode(head)
    
  # iteratively find the first in the list in that cycle
  temp = head
  while temp and temp.next:
    if cycle_and_find(cycle_node, temp):
      return True
    temp = temp.next
  
  return False

class Solution(object):
    def hasCycle(self, head):
      return run(head)
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = c

r = Solution().hasCycle(a)
print(r)