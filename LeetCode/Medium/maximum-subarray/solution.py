class Solution:
    def maxSubArray(self, nums):
        # Handle empty input just in case
        if not nums:
            return 0
            
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # If current_sum is negative, starting fresh at nums[i] 
            # is always better than adding a negative number to nums[i]
            current_sum = max(nums[i], current_sum + nums[i])
            
            if current_sum > max_so_far:
                max_so_far = current_sum
                
        return max_so_far
        