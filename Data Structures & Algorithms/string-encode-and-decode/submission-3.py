class Solution:

    def encode(self, strs: List[str]) -> str:
        word=''
        for i in strs:
            word += str(len(i)) + "#" + i
        return word


    def decode(self, s: str) -> List[str]:
        word_sep = []
        counter = 0
        i=0
        while i<len(s):
            counter = i
            while s[counter] != '#':
                counter+=1
            length = int(s[i:counter])
            i = counter + 1
            counter = i + length
            word_sep.append(s[i:counter])
            i = counter
        return word_sep

