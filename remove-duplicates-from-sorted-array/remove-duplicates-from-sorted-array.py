class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = 0
        
        for i in range(1,len(nums)):
            ni = nums[i]
            nj = nums[j]
            
            j = (ni > nj)*(j + 1) + (1-(ni > nj))*j
            nums[j] = (ni > nj)*(ni) + (1-(ni > nj))*nj
                
        
        return j+1
        