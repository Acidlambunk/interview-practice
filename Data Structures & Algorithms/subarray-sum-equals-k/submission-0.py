class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d_nums = {0: 1}
        counter = 0
        prefix = 0
        for num in nums:
            prefix += num
            diff = prefix - k

            counter += d_nums.get(diff, 0)
            d_nums[prefix] = 1 + d_nums.get(prefix,0)
            print(counter)
        return counter            
