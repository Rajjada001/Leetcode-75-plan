# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, ts, curr_sum, prefix):
            if not node:
                return 0
            curr_sum += node.val
            total_paths = prefix.get(curr_sum-ts, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0)+1

            total_paths += dfs(node.left, ts, curr_sum, prefix)
            total_paths += dfs(node.right, ts, curr_sum, prefix)
            prefix[curr_sum] -= 1
            
            return total_paths

        prefix = {0:1}
        return dfs(root, targetSum, 0, prefix)