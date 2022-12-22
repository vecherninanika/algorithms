class Solution(object):
    def trimBST(self, root, low, high):
        """Trim the tree so that all its elements lie in [low, high].

        Args:
            root(TreeNode):  the root of a binary search tree
            low(int): the lowest boundary
            high(int): the highest boundary

        Returns:
            the root of the trimmed binary search tree
        """
        if not root:
            return None
        # если значение узла больше верхней границы, то и все его правые дети 
        # не подойдут (они еще больше). Запускаем ф-цию от левых детей:
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # если значение узла меньше нижней границы, то и все его левые дети 
        # не подойдут (они еще меньше). Запускаем ф-цию от правых детей:
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # чтобы выводил не 0, а null, нужно написать:
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
