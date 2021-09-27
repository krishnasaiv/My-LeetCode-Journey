class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ################### If entire array is non-positive, return the squares of reversed array
        if nums[-1]<=0:
            return([i*i for i in nums[::-1]])
        ################### If entire array is non-negative, return the squares of array
        if nums[0]>=0:
            return([i*i for i in nums])
        
        ################### Else (solution most definitely exists) 
        ######## BINARY SEARCH ########
        ## Find the pair of elements where first element is <0 & 2nd element is >= 0
        l, r = 0, len(nums)-2
        
        while l<=r:
            m = (l+r) // 2
            
            if nums[m] <0 and nums[m+1] >=0:
                break
            elif nums[m] < 0 and nums[m+1] < 0:
                l = m + 1
            else:
                r = m - 1
        ### we know that a solution exists, hence 
        ## nums[i] < 0 for all i in [0, m]
        ## nums[i] >= 0 for all i in [m+1, n-1]
        
        ######## Merge Elements ########
        results = [0]*len(nums)
        
        i, j = m, m+1
        del(l, r, m)
        
        k = 0
        while i>=0  and j<=len(nums)-1:
            iNum, jNum = nums[i]**2, nums[j]**2
            if iNum <= jNum:
                results[k] = iNum
                i -= 1
            else:
                results[k] = jNum
                j += 1
            k += 1
            
        while i>=0:
            results[k] = nums[i]**2
            i -= 1
            k += 1
        
        while j <=len(nums)-1:
            results[k] = nums[j]**2
            j += 1
            k += 1
        
        return(results)
        
        
        
############# Time Complexity: O(n) #############
## 1. Binary Search ---> O(log(n))
## 2. Merge arrays ---> O(n)

############# Space Complexity: O(n) #############
## 1. Space for results --> O(n)
        
        
        
        
        
        ## When asked to find the pair of elemts where the change starts (first bad element or first element that is >=0), consider the given array
        ## A = [a1, a2, a3, a4, ....... an] as an array of consequtive pairs of length n-1
        ## A = [(a1, a2), (a2, a3), (a3, a4), ...... (an-1, an)], In this array all the pairs are homogeneous except for one pair. 
        ## eg: A = [(G, G), (G, G), (G, G), (G, B), (B, B), (B, B), (B, B)]
        ## Now this problem is reduced to a a simple binary search problem where we have to find the element that we want. 
        ## We can run a while loop with condition l <= r (starting with l=0, r=n-2)
        ## If a solution exists, binary search will find a solution with a pair at indices (m, m+1)
        ## If not, our loop exits with l > r
        ## Explicitly handle the cases where a solution doesnot exist by looking at the first & the last items before binary search
        
        
        ########################################################################################################################
        ###########   IGNORE THIS
        ########################################################################################################################
        ####### If a pair of (<0, >=0) numbers exists in the array, we will get their indices
        ####### If such solution doesnot exist, then there are two cases possible ( Summarized below, both of which are handled explicitly above )
        
        #######     Case 1: Array is completely negative. 
        #######         1. Our while loop will always enter the 'elif' statement
        #######         2. In each loop, the size of problem is reduced in half by eleiminating the left half & selecting the right half
        #######         3. Eventually, m will point to the first element of the last pair (n-2, n-1) 
        #######         4. As the last pair is also both -ve, l is shifted to n-1 & r still points to n-2
        #######         5. Loop halts as  r = n-1, l = n-2, m = n-1 
        
        #######     Case 2: Array is completely non-negative. 
        #######         1. Our while loop will always enter the 'else' statement
        #######         2. In each loop, the size of problem is reduced in half by eleiminating the right  half & selecting the left half
        #######         3. Eventually, m will point to the first oelement of the first pair (0, 1) 
        #######         4. As the first pair is also both non -ve, r is shifted to -1 & l still points to 0
        #######         5. Loop halts as r = -1, l = 0, m = 0
        
                 