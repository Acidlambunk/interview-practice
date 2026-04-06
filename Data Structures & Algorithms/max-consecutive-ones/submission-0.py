class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        gmax = 0
        count = 0
        for n in nums:
            if n != 0:
                count += 1
            else:
                count = 0 
            gmax = max(gmax,count)
        return gmax
