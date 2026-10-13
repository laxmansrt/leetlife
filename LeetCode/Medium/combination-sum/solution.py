class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose
                path.append(candidates[i])
                
                # stay at i (reuse allowed)
                backtrack(i, target - candidates[i], path)
                
                # backtrack
                path.pop()
        
        backtrack(0, target, [])
        return result