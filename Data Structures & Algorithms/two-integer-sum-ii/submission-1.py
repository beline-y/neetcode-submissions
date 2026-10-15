class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)
        index1 = 0
        for num in numbers:
            difference = target - numbers[index1]
            if difference in numSet:
                #chercher indice de difference
                for i in range(index1+1, len(numbers)):
                    if numbers[i] == difference:
                        return [index1+1, i+1]
            index1 += 1
        return False