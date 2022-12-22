class Solution(object):
    def findLongestChain(self, pairs):
        """Find the length of longest chain which can be formed.
        
        Args:
            pairs(List[List[int]]): an array of pairs where pairs[i] = [left_i, right_i] and left_i < right_i
    
        Returns:
        int: the length of longest chain which can be formed
        """
        pairs.sort()
        dp = [1] * len(pairs)   # создаем dp, в котором мы будем хранить ответы
        for i in range(len(pairs)):  # pairs[i] будет текущий элемент
            for j in range(len(pairs)-1):   # pairs[j] - предыдущий (если нет - не подойдет под условие)
                if pairs[j][1] < pairs[i][0]:   # если условие задачи удовлетворяется
                    dp[i] = max(dp[i], dp[j] + 1)  
        return max(dp)
