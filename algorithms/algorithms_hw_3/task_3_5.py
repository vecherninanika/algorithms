class Solution(object):
    def binaryTreePaths(self, root):
        """Сложность: O(n).
        
        Args:
            root (TreeNode): the root of a binary tree
            
        Returns:
            List[str]: all root-to-leaf paths
        """
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            curr, num = stack.pop()
            if not curr.left and not curr.right:
                paths.append(num)
            if curr.left:
                stack.append((curr.left, num + '->' + str(curr.left.val)))
            if curr.right:
                stack.append((curr.right, num + '->' + str(curr.right.val)))
            
        return paths
