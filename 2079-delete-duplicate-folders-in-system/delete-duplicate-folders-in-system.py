class Node:
    __slots__ = ('ch','id')
    def __init__(self):
        self.ch = {}
        self.id = 0

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        
        def dfs(u):
            nonlocal nxt
            items = []
            for k in sorted(u.ch):
                cid = dfs(u.ch[k])
                items.append((k,cid))
            key = tuple(items)
            if key not in idxMap:
                idxMap[key] = nxt
                nxt += 1
            u.id = idxMap[key]
            cnt[u.id] = cnt.get(u.id,0) + 1
            return u.id
            
        def collect(u, path):
            for k, v in u.ch.items():
                node = u.ch[k]
                if node.ch and cnt[node.id] > 1:
                    continue
                newp = path + [k]
                ans.append(newp)
                collect(node, newp)
        
        root = Node()
        for p in paths:
            curr = root
            for d in p:
                if d not in curr.ch:
                    curr.ch[d] = Node()
                curr = curr.ch[d]
        idxMap = {}
        cnt = {}
        nxt = 1
        
        dfs(root)
        ans = []
        collect(root, [])
        return ans