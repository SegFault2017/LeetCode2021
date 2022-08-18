# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def __init__(self):
        self.pairs = defaultdict(list)
        return

    def depthOfTree(self, node) -> int:
        if not node:
            return 0
        l_depth = self.depthOfTree(node.left)
        r_depth = self.depthOfTree(node.right)
        depth = max(l_depth, r_depth) + 1
        self.pairs[depth].append(node.val)
        return depth

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output =[]
        self.depthOfTree(root)
        
        for _, val in self.pairs.items():
            output.append(val)
        return output
        
