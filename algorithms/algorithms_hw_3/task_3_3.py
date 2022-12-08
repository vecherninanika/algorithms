def averageOfLevels(root):
    """Сложность: O(n).
    
    Args:
        root(TreeNode):  the root of a binary tree
        
    Returns:
        List[float]: the average value of the nodes on each level 
    """
    if root == None:   # если дерево пустое
        return []
    cnt_nodes, summ = 0, 0
    ans = []
    queue = [root]
    extra_queue = []
    while queue:
        node = queue.pop()
        cnt_nodes += 1    # считает количество вершин на одном уровне
        summ += node.val  # считает сумму значений вершин на одном уровне
        # если есть левый или правый ребенок, добавляем их в другую очередь, которая потом станет основной:
        if node.left:
            extra_queue.insert(0, node.left)
        if node.right:
            extra_queue.insert(0, node.right)
        if not queue:   # когда вершин на этом уровне больше нет
            ans.append(summ / cnt_nodes)  # добавляем в ответ среднее арифметическое уровня
            cnt_nodes, summ = 0, 0  # обнуляем счетчики
            queue = extra_queue   # теперь дополнительная очередь, в кот. мы записывали детей, станет основной 
            extra_queue = []  # обнуляем дополнительную очередь
    return ans
