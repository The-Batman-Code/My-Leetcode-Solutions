# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = {}
        l = 1
        q = collections.deque([root])

        while q:
            s = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    s += node.val
                    q.append(node.left)
                    q.append(node.right)
            if q:
                res.update({l: s})
                l += 1
        print(res)
        ans = max(res.values())
        print(res.values().index(ans))
        return res.values().index(ans) + 1


# Time : 257ms (27.77%) Space : 20.04 MB (15.37%)
