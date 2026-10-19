##I would implement a bucket sort, so have multiple buckets with size 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        final = []
        finale = []
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        final = [[] for i in range(len(nums)+1)]
        for i in freq:
            final[freq[i]].append(i)
        for i in final[::-1]:
            if i == []:
                continue
            elif k>0:
                finale.extend(i)
                k = k-len(i)
        return finale 

            




        




        
        


        