from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_graph = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            emails = account[1:]
            for email in emails:
                account_graph[email].append(first_email)
                account_graph[first_email].append(email)
        def dfs(graph):
            cc = 0
            component = {}
            visited = set()
            for v in graph:
                if v not in visited:
                    cc += 1
                    explore(graph, v, visited, cc, component)
            return component

        def explore(graph, v, visited, cc, component):
            visited.add(v)
            component[v] = cc
            for neighbour in graph[v]:
                if neighbour not in visited:
                    explore(graph, neighbour, visited, cc, component)

        component = dfs(account_graph)
        group = defaultdict(list)
        res = []

        for vertice, component_num in component.items():
            group[component_num].append(vertice)
        print(group)
        group_list = list(group.values())
        print(group_list)

        for group in group_list:
            target = group[0]
            for account in accounts:
                name = account[0]
                emails = account[1:]
                if target in emails:
                    group.insert(0, name)
                    break
        return group_list







        