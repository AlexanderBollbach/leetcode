def pathSum(tree, sum):
    if tree == None:
        return []

    if tree.left == None and tree.right == None:
        if sum - tree.val == 0:
            return [[tree.val]]
        else:
            return []

    rPaths = []
    lPaths = []

    if tree.left:
        lPaths = [[tree.val] + p for p in pathSum(tree.left, sum - tree.val)]

    if tree.right:
        rPaths = [[tree.val] + p for p in pathSum(tree.right, sum - tree.val)]

    return lPaths + rPaths


class Solution(object):
    def pathSum(self, root, sum):
        return pathSum(root, sum)
        
