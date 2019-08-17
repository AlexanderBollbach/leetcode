class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def log(head):
    temp = head
    while temp:
            print(temp.val)
            temp = temp.next

def insert(head, node):
    if node.val <= head.val:
        node.next = head
        return node

    if not head.next and node.val >= head.val:
        head.next = node
        return head

    curr = head
    second = head.next 

    while curr:
        if not second and node.val >= curr.val:
            curr.next = node
            return head
        
        if node.val >= curr.val and node.val <= second.val:
            curr.next = node 
            node.next = second
            return head

        curr = curr.next
        second = second.next


def sort(head):
    sorted_node = head
    temp = head.next 
    head.next = None 

    while temp:
        n = temp 
        temp = temp.next
        n.next = None
        sorted_node = insert(sorted_node, n)
    return sorted_node

class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return None
        return sort(head)
        
        
a = ListNode(1)
b = ListNode(5)
c = ListNode(3)
d = ListNode(2)
e = ListNode(7)
f = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

r = Solution().insertionSortList(a)
print('==')
log(r)
