def numEnclaves(grid):
    """Сложность: m*n

    Args:
        grid(List[List[int]]): an m x n binary matrix, where 0 is a sea cell and 1 is a land cell

    Returns:
        int: the number of land cells in grid for which we cannot walk off the boundary of the grid
    """
    def f(row, col):
        """Function that changes 1s that are near the boundary to 0s.
        
        Args:
            row(int): the row of the grid
            col(int): the column of the grid
            
        Returns:
            None
        """
        grid[row][col] = 0    # с этой координаты можно выйти за границу. Приравниваем ее к воде.
        if row-1 >= 0 and grid[row-1][col] == 1:   #если соседняя верхняя тоже = 1
            f(row-1, col)   #рекурсивно вызываем эту функцию от нее
        if row+1 < len(grid) and grid[row+1][col] == 1:  #если соседняя нижняя тоже = 1
            f(row+1, col)
        if col-1 >= 0 and grid[row][col-1] == 1:    #если соседняя левая тоже = 1
            f(row, col-1)
        if col+1 < len(grid[0]) and grid[row][col+1] == 1:   #если соседняя правая тоже = 1
            f(row, col+1)

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):  #проходимся по всей матрице
            if grid[0][j] == 1:  #если клетка из самого верхнего ряда = 1
                f(0, j)  #вызываем от нее верхнюю функцию (она станет 0, т.к. с нее можно попасть на землю)
            if grid[i][0] == 1:  #если клетка из самого левого столбца = 1
                f(i, 0)
            if grid[m-1][j] == 1:  #если клетка из самого нижнего ряда = 1
                f(m-1, j)
            if grid[i][n-1] == 1:  #если клетка из самого правого столбца = 1
                f(i, n-1)
     
    return sum(sum(row) for row in grid)   #сумма единиц, оставшихся в матрице
