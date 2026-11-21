class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        es = "".join(char for char in s if char.isalnum())
        rs =es[::-1]
        return es == rs
