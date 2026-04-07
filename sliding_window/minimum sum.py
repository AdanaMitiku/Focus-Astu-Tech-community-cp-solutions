class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)+1
        mi=n+1
        
        l,r,x=0,0,0
        
        for r in range(len(nums)):

            x+=nums[r]
            while x>=target:

                mi=min(mi,r-l+1)
                x-=nums[l]
                l+=1
        return (0 if mi==n+1 else mi)



        
