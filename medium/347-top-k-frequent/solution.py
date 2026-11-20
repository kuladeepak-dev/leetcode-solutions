from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        list1 = Counter(nums).most_common(k)
        list2 = []
        for i in range(len(list1)):
            list2.append(list1[i][0])
        return list2