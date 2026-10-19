class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, v in enumerate(nums):
            if(i != 0 and v == nums[i-1]):
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                threesum = v + nums[left] + nums[right]
                if(threesum < 0):
                    left += 1
                elif(threesum > 0):
                    right -= 1
                else:
                    result.append([v, nums[left], nums[right]])
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1

        return result
            


        