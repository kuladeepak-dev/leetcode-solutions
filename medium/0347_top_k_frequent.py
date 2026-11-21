from collections import Counter
class SolutionCounter:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        list1 = Counter(nums).most_common(k)
        list2 = []
        for i in range(len(list1)):
            list2.append(list1[i][0])
        return list2

class SolutionDict:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        return  sorted(seen,key = seen.get, reverse = True)[:k]

