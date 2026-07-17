from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cntDiv = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cntDiv[g] += freq[multiple]

        exactPairs = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = cntDiv[g]
            pairs = c * (c - 1) // 2
            multiple = 2 * g
            while multiple <= mx:
                pairs -= exactPairs[multiple]
                multiple += g
            exactPairs[g] = pairs

        prefix = []
        gcdVals = []
        s = 0
        for g in range(1, mx + 1):
            if exactPairs[g]:
                s += exactPairs[g]
                prefix.append(s)
                gcdVals.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcdVals[idx])

        return ans