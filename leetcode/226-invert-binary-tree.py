from binary_tree import TreeNode, prettyPrintTree

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # prettyPrintTree(root)
        if not(root):
            return None
        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
sol = Solution()

node1 = TreeNode(2)
node1.left = TreeNode(1)
node1.right = TreeNode(3)
node2 = TreeNode(7)
node2.left = TreeNode(6)
node2.right = TreeNode(9)
root = TreeNode(4)
root.left = node1
root.right = node2

sol.invertTree(root)
# prettyPrintTree(root)
# prettyPrintTree(sol.invertTree(root))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# prettyPrintTree(root)
# prettyPrintTree(sol.invertTree(root))

# root = TreeNode(None)
# prettyPrintTree(root)
# prettyPrintTree(sol.invertTree(root))