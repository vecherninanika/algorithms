from typing import List

def rob(nums: List[int]) -> int:
    """Сложность: O(n)
    
    Args:
        nums(List[int]): the amount of money of each house
        
    Returns:
        int: the maximum amount of money you can rob tonight without alerting the police.
    """
    if len(nums) == 1:
        return nums[-1]  # если дом только 1, мы только его можем ограбить
    elif not nums:
        return 0   # если домой нет, возвращает 0
    else:
        prev_res = 0   # старый максимум домов, которые можно ограбить
        before_prev_res = 0  # результат еще раньше этого
        for i in nums[1:]:   # проходимся по домам, начиная со второго
            prev_res_copy = prev_res
            prev_res = max(before_prev_res + i, prev_res)  # максимум из 
            before_prev_res = prev_res_copy

        prev_res_2 = 0
        before_prev_res_2 = 0
        for j in nums[:-1]:   # проходимся по домам, начиная с первого, но без последнего
            prev_res_2_copy = prev_res_2
            prev_res_2 = max(before_prev_res_2 + j, prev_res_2)
            before_prev_res_2 = prev_res_2_copy
    
    return max(prev_res, prev_res_2)
