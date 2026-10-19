class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        triplet_set = set()
        for i in range(len(nums)):
            target = -nums[i]
            myset = set()
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                else:
                    remain = target - nums[j]
                    if remain in myset:
                        triplet = sorted([nums[i], nums[j], remain])
                        key = tuple(triplet)
                        if key not in triplet_set:
                            result.append(triplet)
                            triplet_set.add(key)
                    else:
                        myset.add(nums[j])
        return result

        