class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # compression
            x = self.parent[x]

        return x

    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1  # parent of p2 will be p1 as it's higher ranked
            self.rank[p1] += self.rank[p2]  # combine ranks of p2 and p1 to rank of p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # parse the names out of emails before the @ symbol
        # e.g. neetcode@gmail.com --> neetcode

        uf = UnionFind(len(accounts))
        emailToAcc = {}  # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:

                # if email already in emailToAcc hashmap, union the account to index
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                # create the hashmap
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i) # find leader (highest ranked)
            emailGroup[leader].append(e) # add it to list

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
            
        return res