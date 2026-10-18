class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setter = set()
        for val in nums:
            if val in setter:
                return True
            else:
                setter.add(val)
        return False

            