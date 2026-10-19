class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in str_set:
                str_set.remove(s[l])
                l += 1
            str_set.add(s[r])
            length = r - l + 1
            if length > longest:
                longest = length
        return longest
