# have a key dict setup where the sorted key list tuple is the key and the list of letters are the values, implemeentation as follows

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        beth = defaultdict(list)    
        for s in strs:
            lister = [0] * 26
            for char in s:
                lister[ord(char) - ord('a')] += 1
            beth[tuple(lister)].append(s)
        return list(beth.values())
        
        
        
            

        