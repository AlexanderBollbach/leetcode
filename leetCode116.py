def connect(left, right):
    if not left or not right:
        return
    if left != right:
        left.next = right
    connect(left.left, left.right)
    connect(right.left, right.right)
    if left != right:
        connect(left.right, right.left)
        
class Solution(object):
    def connect(self, root):
        connect(root, root)
        return root
        
