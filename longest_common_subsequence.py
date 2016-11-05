# longest-common-subsequence of two strings (i.e: DNA strings, etc.)

# returns the length of an LCS of two string s1 and s2
def LCS_length(s1,s2):
    m = len(s1) + 1
    n = len(s2) + 1
    c = [[0 for col in range(n)] for row in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    return c[m-1][n-1]

# returns the LCS of two string s1 and s2 with its length
def LCS(s1,s2):
    m = len(s1) + 1
    n = len(s2) + 1
    c = [[0 for col in range(n)] for row in range(m)]
    b = [[None for col in range(n)] for row in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "top_left"
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "up"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "left"

    print_LCS(b,s1,len(s1),len(s2))
    return (c[m-1][j-1])

def print_LCS(d,s,l1,l2):
    if l1 == 0 or l2 == 0:
        return ""
    elif d[l1][l2] == "top_left":
        print_LCS(d,s,l1-1,l2-1)
        print(s[l1-1])
    elif d[l1][l2] == "up":
        print_LCS(d,s,l1-1,l2)
    else:
        print_LCS(d,s,l1,l2-1)
