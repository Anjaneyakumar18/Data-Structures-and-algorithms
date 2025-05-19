class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tot=[]
        temp=[]
        def track(open,close):
            if open==close==n:
                tot.append("".join(temp))
                return
            if open<n:
                temp.append("(")
                track(open+1,close)
                temp.pop()
            if close<open:
                temp.append(')')
                track(open,close+1)
                temp.pop()
        track(0,0)
        return tot
