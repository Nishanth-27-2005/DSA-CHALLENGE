class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum = float('-inf')
        
        for num in nums:
            current_sum += num
            maximum = max(maximum, current_sum)
            
            if current_sum < 0:
                current_sum = 0
                
        return maximum


obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))