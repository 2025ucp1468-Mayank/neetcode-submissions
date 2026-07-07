class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for st in strs:
            r="".join(sorted(st))
            if r in dict:
                dict[r].append(st)
            else:
                dict[r]=[st]
        ans=[dict[key] for key in dict ]
        return ans
    