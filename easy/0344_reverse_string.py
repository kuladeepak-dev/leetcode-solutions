#time complexity O(n)
#space complexity O(1) no memory created 
#two ponters approch

class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s) - 1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1    
