class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = piles[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                take_left = piles[i] - dp[j]
                take_right = piles[j] - dp[j - 1]

                dp[j] = max(take_left, take_right)

        return dp[n - 1] > 0