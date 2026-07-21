from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            first_email = account[1]
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                account_graph[email].append(first_email)
                account_graph[first_email].append(email)
        visited = set()  
        def dfs(graph):
            res = []
            for v in graph:
                if v not in visited:
                    component = []
                    explore(graph, v, component)
                    target = component[0]
                    name = email_to_name[target]
                    component.sort()
                    component.insert(0, name)
                    res.append(component)
            return res

        def explore(graph, v, component):
            visited.add(v)
            component.append(v)
            for neighbour in graph[v]:
                if neighbour not in visited:
                    explore(graph, neighbour, component)

        group = dfs(account_graph)
        return group







        