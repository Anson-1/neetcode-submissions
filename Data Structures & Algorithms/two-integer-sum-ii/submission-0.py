class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        numbers.sort()
        index1 = 0
        index2 = n-1
        while index1 < index2:
            s = numbers[index1]+numbers[index2]
            if(s < target):
                index1 += 1
            elif(s > target):
                index2 -= 1
            else:
                break
        return [index1+1, index2+1]

        