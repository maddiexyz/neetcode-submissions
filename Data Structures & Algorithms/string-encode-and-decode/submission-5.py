class Solution:

    def encode(self, strs: List[str]) -> str:
        code = "".join(f"{s}<#>" for s in strs)
        return code

    def decode(self, s: str) -> List[str]:
        return s.split("<#>")[:-1]

