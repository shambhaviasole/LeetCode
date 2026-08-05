class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            method = stack.pop()

            for nxt in graph[method]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    stack.append(nxt)

        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]