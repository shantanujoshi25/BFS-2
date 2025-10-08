# // Time Complexity : O(n)
# // Space Complexity : O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root is None):
            return []
        q = [root]
        result = []
        while(len(q) > 0):
            temp = q.copy()
            q = []
            result.append(temp[-1].val)
            for i in temp:
                if(i.left):
                    q.append(i.left)
                if(i.right):
                    q.append(i.right)
        return(result)
                

        