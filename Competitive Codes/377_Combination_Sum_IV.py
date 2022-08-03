def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # for the memorization
        memory = dict()
        
        # backtrack function
        def backTracking(total,memory):
            
            # if total is gerater than the target then current path is invalid return 0
            if total > target:
                return 0
            
            # if current path is equal to target the 1 path is found so return 1
            if total == target:
                return 1
            
            # check if current total is already encountered and stored in memory then return the count
            if total in memory:
                return memory[total]
            
            # count variable to store the number of paths 
            count = 0
            for ele in nums:
                
                # call the backTrack function and their result to the count 
                count += backTracking(total + ele,memory)
            
            # store the number of paths found in the current at current total in memory
            memory[total] = count
            
            # return the count
            return count
        
        # call the backtrack function 
        ans = backTracking(0,memory)
        
        # return the answer
        return ans
