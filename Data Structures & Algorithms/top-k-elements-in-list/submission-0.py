class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for key in nums:
            if key in count:
                count[key]+=1
            else: 
                count[key]=1
        lst=[[] for i in range(len(nums)+1)]
        for key in count:
            lst[count[key]].append(key)
        ans=[]
        for x in range(len(nums),0,-1):
            for r in lst[x]:
                if k==0:
                    break
                else:
                    ans.append(r)
                    k-=1
        return ans

