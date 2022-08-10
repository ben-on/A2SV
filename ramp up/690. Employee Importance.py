"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic={}
        for i in employees:
            dic[i.id]=[i.importance,i.subordinates]
        stk=[dic[id]]
        ans=0
        while stk:
            temp=stk.pop()
            ans+=temp[0]
            for i in temp[1]:
                stk.append(dic[i])
        return ans  