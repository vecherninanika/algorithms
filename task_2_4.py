from typing import List

def maxScoreSightseeingPair(values: List[int]) -> int:
    """Сложность: O(n).

    Args:
        values(List[int]): values of sightseeing spots
        
    Returns:
        int: the maximum score of a pair of sightseeing spots"""
    max_score = 0
    cur_max = 0
    for i in range(1, len(values)):
        cur_max = max(cur_max, values[i-1] + i - 1)
        max_score = max(max_score, cur_max + values[i] - i)
    return max_score
