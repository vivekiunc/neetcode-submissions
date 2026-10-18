# first store a dictionary with key  as the values of dict and values as keys of dict
# Then I would store the difference in another dictionary with values as keys and keys as values
# Then I would loop through one more time to see if each value has a diff thats in the dictionary and if it is then compare the index values and if same then pass, but if different then return 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for k, v in enumerate(nums):
            tracker[v] = k
        for k,v in enumerate(nums):
            diff = target - v
            if diff in tracker and tracker[diff] != k:
                return [k,tracker[diff]]
        return []

        