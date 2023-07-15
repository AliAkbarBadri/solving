# https://leetcode.com/problems/same-tree

from collections import deque
from binary_tree import TreeNode, prettyPrintTree, stringToTreeNode


class Solution:
    # recursive
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p) or not (q):
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

sol = Solution()

tree1 = stringToTreeNode("[1,2,3]")
tree2 = stringToTreeNode("[1,2,3]")
assert (sol.isSameTree(tree1, tree2) == True)

tree1 = stringToTreeNode("[1,2]")
tree2 = stringToTreeNode("[1,null,2]")
assert (sol.isSameTree(tree1, tree2) == False)

tree1 = stringToTreeNode("[1,2,1]")
tree2 = stringToTreeNode("[1,1,2]")
assert (sol.isSameTree(tree1, tree2) == False)
