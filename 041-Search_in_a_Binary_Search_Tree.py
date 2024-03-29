# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        q = collections.deque([root])
        l = []

        def helper(root2):
            q2 = collections.deque([root2])
            while q2:
                l.append(q2.popleft().val)
            print(l)
            return l

        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    if node.val == val:
                        return node
        return


# Time : 55ms (31.30%) Space : 15.46 MB (86.64%)
