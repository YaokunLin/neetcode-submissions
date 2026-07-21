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
     

        for vertice, component_num in component.items():
            group[component_num].append(vertice)
        group_list = list(group.values())
  

        for group in group_list:
            group[1:] = sorted(group[1:])
            target = group[0]
            name = email_to_name[target]
            group.insert(0, name)
        return group_list







        