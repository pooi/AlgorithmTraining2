# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        qu = queue.Queue()
        qu.put(cloned)
        while not qu.empty():
            node = qu.get()
            if node.val == target.val:
                return node
            if node.left is not None:
                qu.put(node.left)
            if node.right is not None:
                qu.put(node.right)
        return None
