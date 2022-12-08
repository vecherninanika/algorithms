class Solution(object):
    def diameterOfBinaryTree(self, root):
        """Сложность: O(n).
    
        Args:
        root(TreeNode):  the root of a binary tree
        
        Returns:
        List[float]: the length of the diameter of the tree (the longest path between any two nodes)
        """
        self.ans = 0   # переменная вне функции, в которой будет храниться ответ
        def func(node):
            if not node:  #если это вершина под листом, то есть None, то глубина будет 0
                return 0
            # рекурсивно вызываем ту же функцию от ребенка этой вершины. Эти две переменные хранят глубину.
            left_depth = func(node.left)
            right_depth = func(node.right)
            self.ans = max(self.ans, left_depth + right_depth + 1)  # максимум из предыдущего результата и суммы глубин детей + вершина
            return max(left_depth, right_depth) + 1   #возвращает макс. глубину этой вершины (макс. глубина среди детей + эта вершина)
        func(root)
        return self.ans - 1    # длина пути-эта вершина (так во всех примерах)
