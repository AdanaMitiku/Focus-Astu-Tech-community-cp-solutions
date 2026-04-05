class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            mn=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[mn]:
                    mn=j
            nums[mn],nums[i]=nums[i],nums[mn]
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a
