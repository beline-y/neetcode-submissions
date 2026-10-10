class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count_table = {}
        for n in nums:
            Count_table[n] = 1 + Count_table.get(n,0)
        
        arr = []
        for num,cnt in Count_table.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
