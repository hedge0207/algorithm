def palindromeIndex(s):
    n = len(s)
    ans = -1
    st, ed = 0, n-1
    while st <= ed:
        if s[st] != s[ed]:
            if ans != -1:
                return -1
            if s[st+1] == s[ed] and s[st+2] == s[ed-1]:
                ans = st
                st += 1
            elif s[st] == s[ed-1] and s[st+1] == s[ed-2] :
                ans = ed
                ed -= 1
            else:
                return -1
        ed -= 1
        st += 1
    return ans