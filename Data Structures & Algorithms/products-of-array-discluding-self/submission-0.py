class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        #Initialisation
        product = 1
        for i in range(1, n):
            product *= nums[i]
        res[0] = product

        for i in range(1,n):
            if nums[i] == 0:
                product = 1
                for j in range(n):
                    if j != i:
                        product *= nums[j]
                res[i] = product
            else:
                res[i]=res[i-1]*nums[i-1]//nums[i]
        return res