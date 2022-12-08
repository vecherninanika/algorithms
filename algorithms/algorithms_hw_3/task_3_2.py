def numEnclaves(grid):
    """Сложность: m*n

    Args:
        grid(List[List[int]]): an m x n binary matrix, where 1 is a sea cell and 0 is a land cell

    Returns:
        int: he number of islands totally (all left, top, right, bottom) surrounded by 1s
    """
    # код как в первом задании:
    def f(row, col):
        """Function that changes 0s that are near the boundary to 1s.
        
        Args:
            row(int): the row of the grid
            col(int): the column of the grid
            
        Returns:
            None
        """
        grid[row][col] = 1    # с этой координаты можно выйти за границу. Приравниваем ее к воде.
        if row-1 >= 0 and grid[row-1][col] == 0:   #если соседняя верхняя тоже = 0
            f(row-1, col)   #рекурсивно вызываем эту функцию от нее
        if row+1 < len(grid) and grid[row+1][col] == 0:  #если соседняя нижняя тоже = 0
            f(row+1, col)
        if col-1 >= 0 and grid[row][col-1] == 0:    #если соседняя левая тоже = 0
            f(row, col-1)
        if col+1 < len(grid[0]) and grid[row][col+1] == 0:   #если соседняя правая тоже = 0
            f(row, col+1)

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):  #проходимся по всей матрице
            if grid[0][j] == 0:  #если клетка из самого верхнего ряда = 0
                f(0, j)  #вызываем от нее верхнюю функцию (она станет 0, т.к. с нее можно попасть на землю)
            if grid[i][0] == 0:  #если клетка из самого левого столбца = 0
                f(i, 0)
            if grid[m-1][j] == 0:  #если клетка из самого нижнего ряда = 0
                f(m-1, j)
            if grid[i][n-1] == 0:  #если клетка из самого правого столбца = 0
                f(i, n-1)
    # код, добавленный к первому заданию, чтобы решить второе:
    count = 0
    for i in range(m):   
        for j in range(n):  #проходимся опять по всей матрице
            if grid[i][j] == 0:  # если клетка - часть острова
                f(i, j)  
#вызываем от нее верхнюю функцию: все клетки, относящиеся к этому острову, станут = 1 и больше в этот if не войдут
                count += 1  #прибавляем полученный остров к count
               
    return count
