class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        d=c.most_common(k)
        result=[e for e,f in d]
        return result





        
