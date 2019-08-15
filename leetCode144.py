# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(tree):
  if not tree:
    return []
  return preorder(tree.left) + [tree.val] + preorder(tree.right)


def preorder_itr(tree):
  s = [tree]
  ls = []
  while True:
    if not s:
      return ls

    last = s[-1]
    s = s[0:-1]
    ls.append(last.val)
  
    if last and last.right:
      s.append(last.right)
    if last and last.left:
      s.append(last.left)

class Solution(object):
    def preorderTraversal(self, root):
        r1 = preorder(root)
        r2 = preorder_itr(root)
        print(r1)
        print(r2)
        return r1
        
t1 = TreeNode(1)

l = TreeNode(2)
r = TreeNode(3)

t1.left = l 
t1.right = r

l.left = TreeNode(4)
l.right = TreeNode(5)

r.left = TreeNode(6)
r.right = TreeNode(7)

r.right.left = TreeNode(8)
r.right.right = TreeNode(9)

r = Solution().preorderTraversal(t1)
# print(r)