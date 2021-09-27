class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        activeOnes = False
        maxConseqOnes = 0
        runningConseqOnes = 0
        for i in range(len(nums)+1):
            if i == len(nums) or nums[i] == 0:
                if activeOnes:
                    maxConseqOnes = max(maxConseqOnes, runningConseqOnes)
                    activeOnes = False
                    runningConseqOnes = 0
            else:
                if not activeOnes:
                    activeOnes = True
                    
                runningConseqOnes += 1
            
            # print(activeOnes, runningConseqOnes, maxConseqOnes)
        
        return(maxConseqOnes)

############# Time Complexity: O(n) #############
## 1. Loop once through the array ---> O(n)

############# Space Complexity: O() #############
## 1. No Extra Space ---> O(1)