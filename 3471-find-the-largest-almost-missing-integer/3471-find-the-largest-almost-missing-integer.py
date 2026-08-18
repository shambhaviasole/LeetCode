class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = [0] * 51

        for i in range(len(nums) - k + 1):
            window = set(nums[i:i + k])

            for x in window:
                count[x] += 1

        ans = -1

        for x in range(51):
            if count[x] == 1:
                ans = x

        return ans