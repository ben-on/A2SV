class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for i in nums1 :
            ll=[]
            for j in range(len(nums2)) :
                if nums2[j] == i and j < len(nums2)-1 :
                    for k in range(j,len(nums2)) :
                        if nums2[k] > i :
                            ll.append(nums2[k])
            if len(ll) > 0 :
                lst.append(ll[0])
            else :
                lst.append(-1)
                    

                    
        return lst
                    

            