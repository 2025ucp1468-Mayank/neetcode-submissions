class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sum=0
        dct={}
        for i in nums:
            if i in dct:
                return True
            else:
                dct[i]=1
        return False