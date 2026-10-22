class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_max = 0
        appeared = {}
        l = 0
        for r in range(len(s)):
            if s[r] in appeared:
                l = max(appeared[s[r]]+1, l)
            appeared[s[r]] = r
            l_max = max(l_max, r-l+1)
        return l_max