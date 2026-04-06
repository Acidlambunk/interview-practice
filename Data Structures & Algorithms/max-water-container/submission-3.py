class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area of water is tinggi paling pendek * lebar
        #2 <= height.length <= 1000
        #0 <= height[i] <= 1000
        left , right = 0 , len(heights) - 1
        max_a = 0
        list_1 = []
        while left < right:
            h = min(heights[left],heights[right])
            w = right - left
            area = w * h
           
            max_a = max(max_a,area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return max_a