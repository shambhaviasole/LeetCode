class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        n=max(nums)
        missing=[i+1 for i in range(m,n) if i+1 not in nums]
        return missing