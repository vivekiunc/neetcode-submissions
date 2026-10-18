class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}
        for char in s:
            if char not in checker:
                checker[char] = 1
            else:
                checker[char] +=1
        blud = {}
        for char in t:
            if char not in blud:
                blud[char] = 1
            else:
                blud[char] += 1
        if checker == blud:
            return True
        else:
            return False
        