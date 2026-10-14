class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if  n == 0:
            return 0
        nums.sort()
        longest = 1
        current = 1
        #unique list
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        
        return longest
