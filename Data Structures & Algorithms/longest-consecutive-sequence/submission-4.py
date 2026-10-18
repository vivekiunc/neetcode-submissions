class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = []
        i=0
        streak = 1
        max_str = 1
        num_set = set(nums)
        num_set = sorted(num_set)
        if len(num_set) == 0:
            return 0

        while i+1 < len(num_set):
            if num_set[i+1]-num_set[i] == 1:
                streak += 1
            else:
                max_str = max(max_str, streak)
                streak = 1
            i += 1

        return max(max_str, streak)
                 

        