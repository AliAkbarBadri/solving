# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque
from binary_tree import TreeNode, prettyPrintTree, stringToTreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ############# DFS - RECURSION ###########################
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        ########################## BFS ########################
        # if not root: 
        #     return 0
        # q = deque()
        # q.append(root)
        # depth = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth += 1
        # return depth

        ############### ITERATIVE - DFS ######################
        # if not root:
        #     return 0

        # st = [[root,1]]
        # maxdepth = 1
        # while st: 
        #     node, depth = st.pop()

        #     if node:
        #         maxdepth = max(depth,maxdepth)
        #         st.append([node.left, depth+1])
        #         st.append([node.right, depth+1])
        # return maxdepth
            



sol = Solution()

node = stringToTreeNode("[3,9,20,null,null,15,7]")
# prettyPrintTree(node)
assert (sol.maxDepth(node) == 3)

node = stringToTreeNode("[1,null,2]")
# prettyPrintTree(node)
assert (sol.maxDepth(node) == 2)
