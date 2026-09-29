class Solution:

    def encode(self, strs: List[str]) -> str:
        code = "".join(f"{len(s)}#{s}" for s in strs)
        return code

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=s.find("#",i)
            l=int(s[i:j])
            res.append(s[j+1:j+1+l])
            i=j+1+l
        return res

