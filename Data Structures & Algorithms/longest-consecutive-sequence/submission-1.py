class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_num = sorted(nums)
        max_len = []
        con_len = 0
        for i in range(len(sort_num)):
            if not max_len:
                max_len.append(sort_num[i])
                if(len(max_len) > con_len):
                        con_len = len(max_len)
            else:
                if(sort_num[i] - max_len[-1] == 1):
                    max_len.append(sort_num[i])
                    if(len(max_len) > con_len):
                        con_len = len(max_len)
                elif (sort_num[i] - max_len[-1] > 1):
                    max_len = []
                    max_len.append(sort_num[i])
                else:
                    continue
        return con_len
        