class Solution(object):
    def minDistance(self, word1, word2):
        """Find the minimum number of steps required to make word1 and word2 the same.

        Args:
            word1(str): first word
            word2(str): second word

        Returns:
            int: the minimum number of steps required 2 words the same
        """
        # Создаем dp размером больше длин слов на 1
        dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
        # Заполняем первую строку и первый столбец количеством операций,
        # необходимых чтобы поменять буквы (0, 1, 2, 3)
        for i in range(len(word1)+1):
            dp[0][i] = i
        for j in range(len(word2)+1):
            dp[j][0] = j
        for row in range(1, len(dp)):  # берем с 1, потому что первую (0) менять не нужно
            for col in range(1, len(dp[0])):
                # Если буквы совпадают:
                if word1[col-1] == word2[row-1]:  # -1, потому что тут нам нужна 0 буква тоже
                    dp[row][col] = dp[row-1][col-1]  # то количество шагов не меняем
                else:  # Если буквы разные, берем минимум предыдущих шагов + 1 (текущий)
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + 1
        return dp[-1][-1]
