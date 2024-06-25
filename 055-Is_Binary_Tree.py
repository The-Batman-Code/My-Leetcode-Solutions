# Approach -1
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    if not root:
        return True
    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    return checkBST(root.left) and checkBST(root.right)


# Approach -2
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from collections import deque


def checkBST(root):
    if not root:
        return False
    if root.left is None and root.right is None:
        return False
    if root.left is None or root.right is None:
        return False
    q = deque([root])
    while q:
        l = len(q)
        for i in range(l):
            node = q.popleft()
            if node:
                if node.left and node.left.data > node.right.data:
                    return False
                q.append(node.left)
                q.append(node.right)


# Approach -3
# A tree is a binary tree if its inorder traversal is sorted
a = []


def checkBST(root):
    if not root:
        return True

    def inorder(root):
        if root.left:
            inorder(root.left)
        a.append(root.data)
        if root.right:
            inorder(root.right)

    inorder(root)
    return a == sorted(list(set(a)))
