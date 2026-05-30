class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for i in strs:
            op+=str(len(i))+"#"+i
        return op


    def decode(self, s: str) -> List[str]:
        op=[]
        while s:
            i=s.find("#")
            length=int(s[:i])
            op.append(s[i+1:i+1+length])
            s=s[i+1+length:]
        return op
