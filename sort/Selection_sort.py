class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            key=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[key]:
                    key=j
            arr[key],arr[i]=arr[i],arr[key]
            
        return arr
