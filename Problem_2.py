# // Time Complexity : O(n)
# // Space Complexity : O(h)
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if(root is None):
            return []
        
        q = [[root]]
        
        while(len(q) > 0):

            result = {}
            
            temp = q.copy()
            q = []

            for i in range(len(temp)):

                for j in temp[i]:
                    if(j.val == x or j.val == y):
                        result[j.val] = i
                    children = []
                    if(j.left):
                        children.append(j.left)
                    if(j.right):
                        children.append(j.right)
                    q.append(children)

            if(x in result and y in result):
                if(result[x] == result[y]):
                    return False
                else:
                    return True
        
        return False


        

    