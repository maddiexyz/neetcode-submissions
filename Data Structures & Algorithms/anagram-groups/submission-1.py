class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freq(s:str)->Tuple[int]:
            freq=[0]*26
            for c in s:
                freq[ord(c)-97]+=1
            return tuple(freq)
        res = {}
        for s in strs:
            f = freq(s)
            if f in res:
                res[f].append(s)
            else:
                res[f]=[s]
        return list(res.values())