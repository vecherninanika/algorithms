from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    """Сложность: O((m+1) * (n+1))
    
    Args:
        obstacleGrid(List[List[int]]): an m x n integer array where an obstacle and space are marked as 1 or 0 respectively 
    
    Return:
        int: the number of possible unique paths that the robot can take to reach the bottom-right corner
    """
    matrix = [[0] * (len(obstacleGrid[0]) + 1) for l in range(len(obstacleGrid) + 1)] # создает матрицу размера как obstacleGrid
    matrix[0][1] = 1 
    for i in range(1, len(obstacleGrid)+1):
        for j in range(1, len(obstacleGrid[0])+1):
            if obstacleGrid[i-1][j-1] == 0:
                matrix[i][j] = matrix[i-1][j] + matrix [i][j-1]

    return matrix[-1][-1]
