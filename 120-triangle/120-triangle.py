class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) == 1:
            return(triangle[0][0])
        # minSumArray = [[0] * i for i in range(1, len(triangle)+1) ]
        # minSumArray[0] = triangle[0]        
        
        for rowNum in range(1, len(triangle)):
            for itemNum in range(len(triangle[rowNum])):
                ep1, ep2 = itemNum-1, itemNum
                # print((rowNum, itemNum), (ep1, ep2))
                
                triangle[rowNum][itemNum]  =triangle[rowNum][itemNum] + min( float('inf') if ep1<0 or ep1>rowNum-1 else triangle[rowNum-1][ep1], float('inf') if ep2<0 or ep2>rowNum-1else triangle[rowNum-1][ep2])
                        
        return(min(triangle[-1]))

        
                
                
                
                
        
        