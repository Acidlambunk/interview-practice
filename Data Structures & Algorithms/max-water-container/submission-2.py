class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area of water is tinggi paling pendek * lebar
        left , right = 0 , len(heights) - 1
        max_a = 0
        list_1 = []
        while left < right:
            h = min(heights[left],heights[right])
            w = right - left
            area = w * h
            list_1.append(area)
            print(list_1)
            max_a = max(list_1)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return max_a