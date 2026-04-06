class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()

        #two pointer approach set pointer left and right then you add left and right 
        #the resultant then is result + x = 0 if x in nums return ...
        #how do we set distinct triplet
        for i, a in enumerate(nums):
            if a > 0:
                break 
            if i > 0 and a == nums[i-1]:
                continue
         
            left , right = i + 1, len(nums) - 1
            while left < right:
                sisa = nums[i] + nums[left] + nums[right]
                if sisa > 0:
                    right -= 1
                elif sisa < 0:
                    left += 1
                else:
                    output.append([a,nums[left],nums[right]])
                    left += 1
                    right -=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return output