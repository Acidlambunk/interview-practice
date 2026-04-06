class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            sisa = target - num
            if sisa in nums_map:
                return [nums_map[sisa],i]
            nums_map[num] = i