from collections import deque

def is_bipartite(graph):
    if not graph:
        return True

    n = len(graph)
    colors = [0] * n

    for i in range(n):
        if colors[i] == 0:
            queue = deque([i])
            colors[i] = 1

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

    return True

# Example usage:
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
    4: [5],
    5: [4],
}

result = is_bipartite(graph)
print("Is the graph bipartite?", result)
