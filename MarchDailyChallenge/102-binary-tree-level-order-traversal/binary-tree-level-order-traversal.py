# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    # res.append(curr.left)
                    q.append(curr.left)
                if curr.right:
                    # res.append(curr.right)
                    q.append(curr.right)
                level.append(curr.val)
            res.append(level)
        return res