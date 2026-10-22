#turn it to a set, iterate through, if target-i in the set and not equal to i, then return then return it
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            if sum > target:
                right -= 1
            if sum == target:
                return [left+1, right+1]
            
            



        