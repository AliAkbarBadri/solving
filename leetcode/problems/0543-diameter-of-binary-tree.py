# https://leetcode.com/problems/diameter-of-binary-tree/

from binary_tree import TreeNode, stringToTreeNode, prettyPrintTree


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res


sol = Solution()

tree = stringToTreeNode("[1,2,3,4,5]")
assert sol.diameterOfBinaryTree(tree) == 3

tree = stringToTreeNode("[1,2]")
assert sol.diameterOfBinaryTree(tree) == 1
