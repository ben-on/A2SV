class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        qu = deque()
        lst=[]
        changed.sort()
        for i in changed :
            if len(qu)> 0 and i == qu[0] :
                qu.popleft()
                continue
            else :
                qu.append(i*2)
                lst.append(i)
        
        if qu==deque([])  :
            return lst
        return []
                
            
        
        
        
        
        
        
        
        # lst=[]
        # lst1=[]
        # comp = ['']*len(changed)
        # changed.sort(reverse=True)
        # for i in range(len(changed)) :
        #     for j in range(i,len(changed)) :
        #         if changed[i] !='' and changed[i]/2 == changed[j]:
        #             lst.append(changed[j])
        #             changed[i] = ''
        #             changed[j] = ''
        # if changed == comp :
        #     return lst
        # return []
                
        # print(changed)
#         for i in range(len(changed)):
#             for j in range(i): 
#                 if (changed[i]*2)==changed[j] and changed[i]!="":
#                     lst.append(changed[i])
#                     changed[i]=""
#                     changed[j]=""
#         print(lst)
        
#         for k in lst:
#             if k!="":
#                 lst1.append(k)
#         if changed==[""]*len(changed):
#             return lst1
#         return []
                    
        
        
        
        
        # # print(changed)
        # for i in range(len(changed)):
        #     for j in range(i):
        #         if changed[i]*2==changed[j]:
        #             # print(changed[j])
        #             lst1.append(changed[i])
        #             changed[i]=""
        #             changed[j]=""
        # if len(lst1)>2:
        #     lst1[-1],lst1[-2]=lst1[-2],lst1[-1]
        #     lst1.pop()
        # print(changed)
        # # print(lst1)
        # if changed==[""]*len(changed):
        #     return lst1
        # return []