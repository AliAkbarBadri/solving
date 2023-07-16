# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque
from binary_tree import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        que = deque()

        def append_q(node: TreeNode):
            if not (node):
                return
            que.append(node)
            append_q(node.left)
            append_q(node.right)
        append_q(subRoot)
        subroot = subRoot
        while root:
            if root.val == subRoot.val:
                root_temp = root
                subRoot_temp = subRoot
                while subRoot:
                    if root.left and 
                and root.left == subRoot.left and root.right == subRoot.right:
                pass

        return
