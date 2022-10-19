def numberOfSteps(num: int)-> int: 
    '''Сложность: O(n)

    Args: 
        num(int): the number that we need to reduce to zero

    Returns:
        int: the number of steps to reduce it to zero 

    '''
    res = 0         # считает колич. шагов
    while num > 0:  # работает, пока не доведем до нуля
        if num % 2 == 0:  # если число четное
            num = num / 2
        else:                  
            num -= 1
        res += 1 
    return res
