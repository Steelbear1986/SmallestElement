class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums=sorted(nums)
        quit=[( nums[::-1][i] + nums[i]) / 2 for i in range(0,len(nums)//2+1)]
        return min(quit)