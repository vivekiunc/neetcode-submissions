class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for char in s:
            if char.isalnum():
                word += char

        word = word.lower().split()
        word = "".join(word)
        wordy = ''
        for char in word[::-1]:
            wordy += char
        if word == wordy:
            return True
        return False

        