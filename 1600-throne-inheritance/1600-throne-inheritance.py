class RoyalMember:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.kids = list()
    def __str__(self):
        if self.alive:
            return self.name
        
        return "" 

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.AdjList = {kingName: RoyalMember(kingName)}
        
    def birth(self, parentName: str, childName: str) -> None:
        
        self.AdjList[parentName].kids.append(childName)
        self.AdjList[childName] = RoyalMember(childName)

    def death(self, name: str) -> None:
        self.AdjList[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        print(self.AdjList)
        from collections import deque
        InheritanceOrder = []
        q = deque()
        
        q.append(self.kingName)
        while q:
            candidate = q[-1]
            q.pop()
            
            if self.AdjList[candidate].alive:
                InheritanceOrder.append(candidate)
        
            for i in self.AdjList[candidate].kids[::-1]:
                q.append(i)
        
        return InheritanceOrder
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()