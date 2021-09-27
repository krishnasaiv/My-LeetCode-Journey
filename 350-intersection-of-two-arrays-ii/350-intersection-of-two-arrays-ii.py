from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        result = []
        for i in c2:
            if i in c1:
                result += [i] * min(c2[i], c1[i])
        
        return(result)