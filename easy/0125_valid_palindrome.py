 #space complexity O(n)
class Solution1:
    def isPalindrome_v1(self, s: str) -> bool:
        s = s.lower()
        es = "".join(char for char in s if char.isalnum())
        rs =es[::-1]
        return es == rs


#space complexity O(1)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower() == s[j].lower(): 
                i+=1
                j-=1
            else:
                return False
        return True
