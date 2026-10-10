class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        n = len(nums)
        for i in range(n):
            number = nums[i]
            difference = target - nums[i]
            if difference in index:
                return [index[difference], i]
            index[number] = i

