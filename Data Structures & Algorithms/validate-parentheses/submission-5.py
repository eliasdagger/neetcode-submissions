class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)
        i = 0
        st = []
        
        while i < len(l):
            if l[i] == "[" or l[i] == "(" or l[i] == "{":
                st.append(l[i])
                i += 1
            else:
                if not st:
                    return False
                peek = st[len(st) -1]
                if (peek == "("  and l[i] == ")") or (peek == "[" and l[i] == "]") or (peek == "{" and l[i] == "}"):
                    st.pop()
                    i +=1
                    continue
                else: 
                    return False
        return len(st) == 0