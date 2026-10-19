class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]*prefix[-1])
        postfix = []
        for num in reversed(nums):
            if not postfix:
                postfix.append(num)
                continue
            postfix.append(num*postfix[-1])
        postfix = list(reversed(postfix))
        result = []
        result.append(postfix[1])
        for i in range(1, len(nums)-1):
            result.append(prefix[i-1]*postfix[i+1])
        result.append(prefix[-2])
        return result
