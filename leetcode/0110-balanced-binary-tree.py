# https://leetcode.com/problems/balanced-binary-tree/


from turtle import right
from binary_tree import TreeNode, stringToTreeNode, prettyPrintTree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced2(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1


sol = Solution()

tree = stringToTreeNode("[3,9,20,null,null,15,7]")
assert sol.isBalanced(tree) == True

tree = stringToTreeNode("[1,2,2,3,null,null,3,4,null,null,4]")
assert sol.isBalanced(tree) == False


tree = stringToTreeNode("[1,2,2,3,3,null,null,4,4]")
assert sol.isBalanced(tree) == False

tree = stringToTreeNode("[]")
assert sol.isBalanced(tree) == True
