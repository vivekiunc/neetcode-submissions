# keep a dict of all values
# if va

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ind = dict()
        for num in nums:
            ind[num] = ind.get(num, 0) + 1
            if ind[num] > 1:
                return True
        return False
            
        