class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
                continue
            prod *= nums[i]
        print(prod)
        if(len(zero) > 1):
            result = [0] * len(nums)
            return result
        elif len(zero) == 1:
            result = [0] * len(nums)
            index = zero[0]
            result[index] = prod
            return result
        else:
            for j in range(len(nums)):
                result.append(int(prod/nums[j]))
            return result