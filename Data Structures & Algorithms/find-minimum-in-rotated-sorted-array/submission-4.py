class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        else:
            while r - l > 1:
                mid = (r + l) // 2
                if nums[mid] < nums[r]:
                    r = mid
                elif nums[mid] > nums[l]:
                    l = mid
        return min(nums[l], nums[r])

        