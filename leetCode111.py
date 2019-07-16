class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getDepth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    if tree.left != None and tree.right == None:
        return getDepth(tree.left) + 1
    if tree.right != None and tree.left == None:
        return getDepth(tree.right) + 1
    
    l = getDepth(tree.left) + 1
    r = getDepth(tree.right) + 1
    return l if l < r else r 

class Solution(object):
    def minDepth(self, root):
        return getDepth(root)
