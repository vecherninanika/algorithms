def minimumAbsDifference(arr: list) -> list:
    '''Сложность: O(nlog(n))

    Args:
        arr(list):  an array of distinct integers

    Return:
        list: pairs of elements with the minimum absolute difference
    '''
    arr.sort()
    min_dif = 10**6
    list_result = []
    for i in range(len(arr)-1):
        dif = arr[i+1] - arr[i]     
        if dif < min_dif:
            min_dif = dif
            list_result.append([arr[i], arr[i+1]])
        elif dif == min_dif:
            list_result.append([arr[i], arr[i+1]])
    return list_result
