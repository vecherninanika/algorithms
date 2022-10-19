def numberOfMatches(n: int) -> int:
    '''Сложность: O(n)

    Args:
        num(int): number of teams

    Return:
        int: number of matches played until a winner is decided
    '''
    parties = 0
    while n > 1:
        if n % 2 == 0:
            parties = parties + n // 2
            n = n // 2
        else:
            parties = parties + (n - 1) // 2
            n = (n - 1) // 2 + 1
    return parties
