class Solution: 
    def select(self, arr, i):
        c=i
        for a in range(i,len(arr)):
            if arr[a]<arr[c]:
                c=a
        return c
        # code here 
    
    def selectionSort(self, arr,n):
        for j in range(len(arr)):
            c1=j
            c=self.select(arr,j)
            arr[c1],arr[c]=arr[c],arr[c1]
        return arr