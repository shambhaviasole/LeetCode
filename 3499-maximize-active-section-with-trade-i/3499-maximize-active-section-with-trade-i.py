class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        initial_ones = s.count('1')

        t = '1' + s + '1'

        groups = []

        i = 0
        while i < len(t):
            j = i

            while j < len(t) and t[j] == t[i]:
                j += 1

            groups.append((t[i], j - i))
            i = j

        ans = initial_ones

        for i in range(1, len(groups) - 1):
            if (groups[i][0] == '1' and
                groups[i - 1][0] == '0' and
                groups[i + 1][0] == '0'):

                left_zero = groups[i - 1][1]
                right_zero = groups[i + 1][1]

                gain = left_zero + right_zero

                ans = max(ans, initial_ones + gain)

        return ans