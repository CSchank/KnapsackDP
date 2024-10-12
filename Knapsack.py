def dynamic_knapsack(wv, W):
    v = {}

    def solve(i,w):
        if (w < 0):
            return float("-inf")
        if (i==0):
            v[i,w] = 0
            return 0
        
        wi = wv[i-1][0]
        vi = wv[i-1][1]

        v[i,w] = max(solve(i-1, w), vi + solve(i-1,w-wi))
        return v[i,w]
    
    solution = solve(len(wv), W)

    return (solution,v)

def backtrack(V,wv):

    def backtrack_(i,w):
        wi = wv[i-1][0]

        if i == 0:
            return []
        
        if V[i,w] == V[i-1,w]:
            return backtrack_(i-1,w) + [0]
        else:
            return backtrack_(i-1,w-wi) + [1]
    
    (n,W) = max(list(V.keys()))
    return backtrack_(n,W)

def renderTable(n,W,V):
    for i in range (n+1):
        for w in range(W+1):
            print(V.get((i,w),'-'), end='\t')
        print("\n")

if __name__ == "__main__":
    wv = [[4,15],[5,17],[3,14],[6,19],[2,11]]
    W = 11

    z, V = dynamic_knapsack(wv, W)

    renderTable(len(wv), W, V)
    print(f"Optimal value: z = {z}")
    print(f"Solution: {backtrack(V, wv)}")
