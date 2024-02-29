# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        max_sum = float('-inf')
        res = 0
        while q:
            level += 1
            curr_sum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                print(curr.val)
                curr_sum += curr.val
                if curr.left:
                    # ls = curr.left.val
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    # rs = curr.right.val
            print(curr_sum)
            if curr_sum > max_sum:
                max_sum = curr_sum
                res = level
            # level += 1

        return res
