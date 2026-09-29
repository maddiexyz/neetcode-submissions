class Solution:

    def encode(self, strs: List[str]) -> str:
        code = "".join(f"{len(s)}#{s}" for s in strs)
        return code

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res=[]
        num=""
        word=""
        while pointer<len(s):
            if s[pointer]=="#":
                for i in range(1,int(num)+1):
                    word+=s[pointer+i]
                res.append(word)
                pointer+=int(num)
                num=""
                word=""
            else:
                num+=s[pointer]
            pointer+=1
        return res

