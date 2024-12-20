# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #so we have to do level traversal right so BFS
        q=deque([root])
        i=0
        while q:
            #here are the modification 
            if i & 1:
                l,r=0,len(q)-1
                while l<r:
                    q[l].val,q[r].val=q[r].val,q[l].val
                    l+=1
                    r-=1
            #standard BFS
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i+=1
        return root                

        