class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights)-1
        left = 0
        area = 0
        maxi = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if heights[left] >= heights[right] and left < right:
                right -= 1
            else:
                left += 1 
            if area > maxi:
                maxi = area
        return maxi
            


        