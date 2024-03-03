# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax, count):
            if not node:
                return 0
            if node.val >= currMax:
                count = 1
            else:
                count = 0
            currMax = max(currMax, node.val)
            count += dfs(node.left, currMax, count)
            count += dfs(node.right, currMax, count)

            return count

        
        return dfs(root, root.val, 0)