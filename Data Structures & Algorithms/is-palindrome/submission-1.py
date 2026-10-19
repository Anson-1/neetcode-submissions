class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_converted = ""
        for ch in s:
            if ch.isalnum():
                s_converted += ch.lower()
        s_reverse = s_converted[::-1]
        if s_reverse == s_converted:
            return True
        else:
            return False