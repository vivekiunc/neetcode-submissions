#I would have a double pointer for the decode, so i would have one at the start and en 
class Solution:

    def encode(self, strs: List[str]) -> str:
        wordle = ''
        for word in strs:
            wordle +=  str(len(word)) + '#' + word
        return wordle
        



    def decode(self, s: str) -> List[str]:
        string = []
        pointer1 = 0
        pointer2 = 0
        counter = ''
        i = 0
        while i<len(s):
            if s[i] == '#':
                length = int(counter)
                pointer1 = i + 1
                pointer2 = pointer1 + length
                string.append(s[pointer1:pointer2])
                i = pointer2
                counter = ''
            else:
                 counter = counter + s[i]
                 i += 1
        return string
                
