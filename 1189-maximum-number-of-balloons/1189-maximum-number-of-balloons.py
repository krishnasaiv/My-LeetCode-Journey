from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7 :
            return(0)
        c = Counter(''.join([ i for i in text if i in 'balon']))
        
        return ( min( min(c['b'], c['a'], c['n']), min(c['l'], c['o']) // 2 ) )