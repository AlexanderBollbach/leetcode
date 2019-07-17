def hasPathSum(tree, sum):
    if tree == None:
        return False
    if tree.left == None and tree.right == None:
        return sum - tree.val == 0

    if tree.left:
        left = hasPathSum(tree.left, sum - tree.val)
        if left:
            return left

    if tree.right:
        right = hasPathSum(tree.right, sum - tree.val)
        if right:
            return right

    return False


class Solution(object):
    def hasPathSum(self, root, sum):
        return hasPathSum(root, sum)
        
