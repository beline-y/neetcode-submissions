class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i_prefix = 0
        i_suffix = n-1
        while i_prefix < i_suffix:
            while i_prefix < i_suffix and not self.alphaNum(s[i_prefix]):
                i_prefix += 1
            while i_prefix < i_suffix and not self.alphaNum(s[i_suffix]):
                i_suffix -= 1
            if s[i_prefix].lower() != s[i_suffix].lower():
                return False
            i_prefix += 1
            i_suffix -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))