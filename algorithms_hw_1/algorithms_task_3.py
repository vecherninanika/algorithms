def numJewelsInStones(jewels: int, stones: int) -> int:
    '''Сложность: O(n)

    Args:
        jewels(int): types of stones that are jewels
        stones(int): the stones I have

    Return:
        int: the number of stones that are also jewels
    '''
    list_jewels = [jewel for jewel in jewels]  #делаем из jewels список
    res = 0
    for i in stones:
        if i in list_jewels:
            res += 1     # прибавляем к результату 1, если камень есть в списке list_jewels
    return res
