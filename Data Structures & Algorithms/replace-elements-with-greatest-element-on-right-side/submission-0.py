class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax=-1
        i=len(arr)-1
        while(i>=0):
            curr=rmax
            if arr[i]>rmax:
                rmax=arr[i]
            arr[i]=curr
            i-=1
        return arr