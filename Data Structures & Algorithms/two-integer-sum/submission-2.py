class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       result = {}
       for i, num in enumerate(nums):
        sisa = target - num
        if sisa in result:
            return [result[sisa],i]
        result[num] = i