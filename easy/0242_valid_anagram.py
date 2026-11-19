class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return (Counter(s)==Counter(t))
    
    
    
class SolutionDict:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch,0)+1
        for ch in t:
            dict2[ch] = dict2.get(ch,0)+1 
        return (dict1 == dict2)
    
    
class SolutionSorted:
    def isAnagram(self, s: str, t: str) -> bool:
        return ((sorted(s)) == sorted(t))
