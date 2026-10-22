class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charSet = {}
        for char in s1:
            charSet[char] = 1 + charSet.get(char, 0)
        need = len(charSet)
        for r in range(len(s2)):
            count = {}
            cur = 0
            for j in range(r, len(s2)):
                count[s2[j]] = 1 + count.get(s2[j], 0)        
                if charSet.get(s2[j],0) < count[s2[j]]:
                    break
                if charSet.get(s2[j],0) == count[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
            
        return False