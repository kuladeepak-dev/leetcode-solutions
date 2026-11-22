class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #space complexity O(n)
        es = "".join(char for char in s if char.isalnum())
        rs =es[::-1]
        return es == rs



class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower() == s[j].lower(): #space complexity O(1)
                i+=1
                j-=1
            else:
                return False
        return True
