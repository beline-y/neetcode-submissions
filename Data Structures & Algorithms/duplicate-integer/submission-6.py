class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        h = set()

        for n in nums:
            if n in h:
                return True
            h.add(n)
        
        return False