# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque
from binary_tree import TreeNode, stringToTreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p) or not (q):
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    ## BFS
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not (subRoot):
            return True
        if not (root):
            return False
        que = deque()
        que.append(root)
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if self.isSameTree(node, subRoot):
                    return True
                if node:
                    que.append(node.right)
                    que.append(node.left)
        return False

    ## recursive
    # def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    #     if not(subRoot):
    #         return True
    #     if not(root):
    #         return False
    #     if self.isSameTree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


sol = Solution()

root = stringToTreeNode("[3,4,5,1,2]")
subRoot = stringToTreeNode("[4,1,2]")
assert sol.isSubtree(root, subRoot) == True

root = stringToTreeNode("[3,4,5,1,2,null,null,null,null,0]")
subRoot = stringToTreeNode("[4,1,2]")
assert sol.isSubtree(root, subRoot) == False
