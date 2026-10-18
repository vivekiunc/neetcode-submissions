class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        maps = []
        for i in counter:
            maps.append([counter[i], i])
        maps.sort()
        res = []
        while len(res) < k:
            res.append(maps.pop()[1])
        return res

            


        