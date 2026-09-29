class Solution:

    def encode(self, strs: List[str]) -> str:
        code = "".join(f"{len(s)}#{s}" for s in strs)
        return code

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res=[]
        numstr=""
        while pointer<len(s):
            if s[pointer]=="#":
                n=int(numstr)
                res.append(s[pointer+1:pointer+n+1])
                numstr=""
                pointer+=n
            else:
                numstr+=s[pointer]
            pointer+=1
        return res

