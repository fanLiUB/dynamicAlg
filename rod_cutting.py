# sovles the rod-cutting problem using dynamic programming

# length i: 1  2  3  4  5  6  7  8  9  10
# price pi: 1  5  8  9  10 17 17 20 24 30

# a recursive top-down implem.
# takes as input a list p of prices and an integer length n
# returns the max revenue possible for cutting a rod w/ length n
# T(n) = 2^n: an exp recursive alg
def cut_rod_recursive(p,n):
    if n == 0:
        return 0
    q = min(p) - 1
    for i in range(n):
        q = max(q, p[i] + cut_rod_recursive(p,n-i-1))
    return q 
    
# a top-down memoizid dynamic solution
def cut_rod_memoized(p,n):
    r = [None] * n
    return cut_rod_mem_helper(p,n,r)

def cut_rod_mem_helper(p,n,r):
    if n == 0:
        return 0
    if r[n-1] != None:
        return r[n-1]
    else:
        q = min(p) - 1
    for i in range(n):
        q = max(q, p[i] + cut_rod_mem_helper(p,n-i-1,r))
    r[n-1] = q
    return q

