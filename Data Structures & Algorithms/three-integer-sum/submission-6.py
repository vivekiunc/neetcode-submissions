class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        final = []
        freq = {}
        start = 0
        left = 1
        right = len(nums) - 1
        for start in range(len(nums)):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            left = start + 1
            right = len(nums) - 1
            while left < right:
                val = nums[start] + nums[left] + nums[right]
                if val > 0: 
                    right -=1
                if val < 0:
                    left += 1
                if val == 0:
                    final.append([nums[start], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return final


        
                
            

        