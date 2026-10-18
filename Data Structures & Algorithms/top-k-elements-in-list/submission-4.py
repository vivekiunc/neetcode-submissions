class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lister = [[] for i in range(len(nums)+1) ]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            lister[value].append(key)
        
        res = []
        for i in range(len(lister) -1, 0, -1):
            for num in lister[i]:
                res.append(num)
                if len(res) == k:
                    return res




        