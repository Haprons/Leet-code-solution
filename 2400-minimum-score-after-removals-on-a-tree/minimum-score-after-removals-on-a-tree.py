class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        tree=[[] for i in range(len(nums))]
        for x,y in edges:
            tree[x].append(y)
            tree[y].append(x)
        xor={}
        child={}
        def rec(root,parent):
            xor[root]=nums[root]
            child[root]=set([root])
            for node in tree[root]:
                if node!=parent:
                    child[root].add(node)
                    child[root]=child[root].union(rec(node,root))
                    xor[root]=xor[root] ^ xor[node] 
            return child[root]
        rec(0,-1)
        V=xor[0]
        res=float('inf')
        for u in range(len(edges)):
            a,b=edges[u]
            if a in child[b]:
                b,a=a,b
            for v in range(u+1,len(edges)):
                c,d=edges[v]
                if c in child[d]:
                    c,d=d,c
                if d in child[b]:
                    cur = [xor[d], xor[b]^xor[d], V^xor[b]]
                elif b in child[d]:
                    cur = [xor[b], xor[d]^xor[b], V^xor[d]]
                else:
                    cur = [xor[b], xor[d], V^xor[b]^xor[d]]
                # res=min(res,max(comp1,comp2,comp3)-min(comp1,comp2,comp3))
                res=min(res,max(cur)-min(cur))
        return res