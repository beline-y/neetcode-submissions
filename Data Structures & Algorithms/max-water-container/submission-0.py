class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        r, l = 0, n-1
        while r<l:
            h1 = heights[r]
            h2 = heights[l]
            h = min(h1,h2)
            res = max(res, h*(l-r))
            if h == h1:
                r += 1
            else:
                l -= 1
        return res
