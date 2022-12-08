from typing import List

def getDescentPeriods(prices: List[int]) -> int:
    """Сложность: O(n).
    
    Args:
        prices(List[int]): an integer representing the daily price history of a stock
    
    Return:
        int: the number of smooth descent periods
    """
    count = 1
    matrix = [1] * len(prices)
    for i in range(1, len(prices)):
        if prices[i] == prices[i-1] - 1:    # если цена меньше вчерашней на 1
            matrix[i] = matrix[i-1] + 1     # записываем в матрицу 1 + предыдущий результат
        count += matrix[i]      # прибавляем полученное значение к предыдущему результату

    return count
