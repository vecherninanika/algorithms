from typing import List
def countSquares(matrix: List[List[int]]) -> int:
    """Return how many square submatrices have all ones. Сложность: O(n**2)

    Args:
        matrix(int): m * n matrix of ones and zeros

    Return:
        int: how many square submatrices have all ones
    """
    dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
    result = 0
    for i in range(1, len(matrix)+1):
        for j in range(1, len(matrix[0])+1):
            if matrix[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                result += dp[i][j]
    return result
