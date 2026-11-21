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
        return sorted(seen,key = seen.get, reverse = True)[:k]


class SolutionBucketSort:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0)+1
        buckets = [[] for _ in range(len(nums)+1)] 
        for num,freq in counts.items():
            buckets[freq].append(num)
        result = []
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result   

