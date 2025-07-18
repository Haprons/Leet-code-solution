class Solution:
    def minimumDifference(self, V: List[int]) -> int:
        n = len(V)//3

        # for each closed range [0,n], ... [0,2n-1] find min. n elements
        ## store their sum
        H = [-v for v in V[:n]]
        heapify(H)
        P = [-sum(H)]                # prefix sum
        for v in V[n: 2*n]:
            p = P[-1]
            if -v > H[0]:
                p -= -heappop(H)
                heappush(H, -v)
                p += v
            P.append(p)
        #print(P)

        # for each range [n,3n], ... [2n,3n] find max. n elements
        ## store their sum
        H = [v for v in V[2*n:]]
        heapify(H)
        S = [sum(H)]                # suffix sum
        for v in V[2*n-1: n-1: -1]:
            s = S[-1]
            if v > H[0]:
                s -= heappop(H)
                heappush(H, v)
                s += v
            S.append(s)
        S = S[::-1]
        #print(S)

        # cost is sum-min(N[0:n-1]) + sum-max(N[n:3n-1]) - closed ranges
        # here P starts at n-1 and S[::-1] ends at n - hence zip directly
        return min(p-s for p,s in zip(P,S))