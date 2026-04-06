class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        b=[]
        for i in range(len(nums)):
            a=0
            key=nums[i]
            for j in range(len(nums)):
                if key>nums[j]:
                    a+=1
            b.append(a)
        return b

        
