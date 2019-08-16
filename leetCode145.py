# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def postorder(tree):
  if not tree:
    return []
  return postorder(tree.left) + postorder(tree.right) + [tree.val]

def postorder_itr(tree):
  stack = [tree]
  ls = []
  while True:
    if len(stack) == 0:
      return ls
    
    last = stack[-1]

    if last and last.left:
      stack.append(last.left)
      continue
    
    if last and last.right:
      stack.append(last.right)
      continue
    
    if last and len(stack) > 1 and stack[-2].left == last:
      stack[-2].left = None
      ls.append(stack[-1].val)
      stack = stack[0:-1]
      continue
    
    if last and len(stack) > 1 and stack[-2].right == last:
      stack[-2].right = None
      ls.append(stack[-1].val)
      stack = stack[0:-1]
      continue
    
    if last and not last.left and not last.right:
      ls.append(stack[-1].val)
      stack = stack[0:-1]
      continue


class Solution(object):
    def postorderTraversal(self, root):
        return postorder_itr(root)
        
t1 = TreeNode(1)

l = TreeNode(2)
r = TreeNode(3)

t1.left = l 
t1.right = r

l.left = TreeNode(4)
l.right = TreeNode(5)

r.left = TreeNode(6)
r.right = TreeNode(7)

# r.right.left = TreeNode(8)
# r.right.right = TreeNode(9)

r = Solution().postorderTraversal(t1)
print(r)