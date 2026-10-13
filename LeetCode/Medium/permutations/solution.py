class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(start):
            # Base case: if start reaches the end, we have a complete permutation
            if start == len(nums):
                result.append(nums[:]) # Append a copy of the current state
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start index
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively call to fix the next position
                backtrack(start + 1)
                
                # Backtrack: swap back to original state
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result