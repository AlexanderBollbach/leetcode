class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(nums):
    head = ListNode(nums[0])
    temp = head
    for i in nums[1:]:
        n = ListNode(i)
        temp.next = n
        temp = n

    return head

def log(head):
    print('===')
    temp = head
    while temp:
            print(temp.val)
            temp = temp.next
    print('===')
    
# 1 3 5
# 2 4
def join_lists(a, b):
    if a.val <= b.val:
        head = a
        a = a.next
    else:
        head = b
        b = b.next

    head.next = None 
    temp = head

    while a or b:
        if a and b and a.val >= temp.val and a.val <= b.val:
            temp.next = a
            temp = a
            a = a.next 
            continue
        if a and b and b.val >= temp.val and b.val <= a.val:
            temp.next = b
            temp = b
            b = b.next
            continue
        if a and a.val >= temp.val:
            temp.next = a
            temp = a
            a = a.next
            continue
        if b and b.val >= temp.val:
            temp.next = b
            temp = b
            b = b.next
            continue
    return head

def sort(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    mid = count / 2

    if count == 2:
        a = head 
        b = head.next
        b.next = None
        a.next = None
        if a.val >= b.val:
            b.next = a
            return b
        else:
            a.next = b
            return a
    elif count == 1:
        return head
    
    temp = head 
    count = 0
    while temp:
        count += 1
        if count == mid:
            break
        temp = temp.next

    upper = temp.next 
    temp.next = None
    
    a = sort(head)
    b = sort(upper)

    return join_lists(a, b)

class Solution(object):
    def sortList(self, head):
        if not head:
            return None
        return sort(head)
        


a = create_list([-1, 5, 3, 4, 0])
c = sort(a)
log(c)
