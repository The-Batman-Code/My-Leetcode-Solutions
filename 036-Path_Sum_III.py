# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def findPathSum(root, s, current_sum):
            if not root:
                return 0
            current_sum += root.val
            if current_sum == s:
                self.total += 1
            findPathSum(root.left, s, current_sum)
            findPathSum(root.right, s, current_sum)

        if not root:
            return 0

        findPathSum(root, targetSum, 0)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.total


# Time : 729ms (28.87%) Space : 13.26 MB (25.60%)
