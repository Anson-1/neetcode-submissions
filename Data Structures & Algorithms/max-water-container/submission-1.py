class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0
        while(r > l):
            if(heights[l] < heights[r]):
                width = r - l
                height = min(heights[l], heights[r])
                area = width * height
                if area > max_area:
                    max_area = area
                l += 1
            else:
                width = r - l
                height = min(heights[l], heights[r])
                area = width * height
                if area > max_area:
                    max_area = area
                r -= 1
        return max_area
        