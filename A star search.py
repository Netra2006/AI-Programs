
import heapq

def a_star(graph, heuristic, start, goal):

    if start not in graph:
        print("Invalid start node")
        return

    if goal not in graph:
        print("Goal node does not exist")
        return

    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    g = {start: 0}
    parent = {start: None}

    while open_list:

        f, current = heapq.heappop(open_list)

        if f != g[current] + heuristic[current]:
            continue

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Path:", path)
            print("Total Cost:", g[goal])
            return

        for neighbour, cost in graph[current].items():

            new_cost = g[current] + cost

            if neighbour not in g or new_cost < g[neighbour]:

                g[neighbour] = new_cost
                parent[neighbour] = current

                new_f = new_cost + heuristic[neighbour]

                heapq.heappush(open_list, (new_f, neighbour))

    print("No path exists")


# Base Graph
graph = {
    'A': {'B': 1, 'C': 2, 'H': 7},
    'B': {'D': 4, 'E': 6},
    'C': {'F': 3, 'G': 2},
    'D': {'E': 7},
    'E': {},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}

# Heuristic Values
heuristic = {
    'A': 5, 'B': 3, 'C': 4, 'D': 2,
    'E': 6, 'F': 3, 'G': 1, 'H': 0
}

# Test Cases
test_cases = [
    ('A', 'H'),
    ('A', 'A'),
    ('A', 'D'),
    ('A', 'F'),
    ('A', 'Z'),
]

print("Test Case 1:")
a_star(graph, heuristic, 'A', 'H')

print("\nTest Case 2:")
a_star(graph, heuristic, 'A', 'A')

print("\nTest Case 3:")
a_star(graph, heuristic, 'A', 'D')

print("\nTest Case 4:")
a_star(graph, heuristic, 'A', 'F')

print("\nTest Case 5:")
a_star(graph, heuristic, 'A', 'Z')

# Test Case 6
print("\nTest Case 6:")

graph6 = {
    'A': {'B': 2},
    'B': {'A': 2},
    'C': {}
}

heuristic6 = {'A': 2, 'B': 1, 'C': 0}

a_star(graph6, heuristic6, 'A', 'C')

# Test Case 7
print("\nTest Case 7:")
a_star(graph, heuristic, 'A', 'H')

# Test Case 8
print("\nTest Case 8:")
a_star(graph, heuristic, 'X', 'H')

import heapq

def a_star(graph, heuristic, start, goal):

    if start not in graph:
        print("Invalid start node")
        return

    if goal not in graph:
        print("Goal node does not exist")
        return

    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    g = {start: 0}
    parent = {start: None}

    while open_list:

        f, current = heapq.heappop(open_list)

        if f != g[current] + heuristic[current]:
            continue

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Path:", path)
            print("Total Cost:", g[goal])
            return

        for neighbour, cost in graph[current].items():

            new_cost = g[current] + cost

            if neighbour not in g or new_cost < g[neighbour]:

                g[neighbour] = new_cost
                parent[neighbour] = current

                new_f = new_cost + heuristic[neighbour]

                heapq.heappush(open_list, (new_f, neighbour))

    print("No path exists")


# Base Graph
graph = {
    'A': {'B': 1, 'C': 2, 'H': 7},
    'B': {'D': 4, 'E': 6},
    'C': {'F': 3, 'G': 2},
    'D': {'E': 7},
    'E': {},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}

# Heuristic Values
heuristic = {
    'A': 5, 'B': 3, 'C': 4, 'D': 2,
    'E': 6, 'F': 3, 'G': 1, 'H': 0
}

# Test Cases
test_cases = [
    ('A', 'H'),
    ('A', 'A'),
    ('A', 'D'),
    ('A', 'F'),
    ('A', 'Z'),
]

print("Test Case 1:")
a_star(graph, heuristic, 'A', 'H')

print("\nTest Case 2:")
a_star(graph, heuristic, 'A', 'A')

print("\nTest Case 3:")
a_star(graph, heuristic, 'A', 'D')

print("\nTest Case 4:")
a_star(graph, heuristic, 'A', 'F')

print("\nTest Case 5:")
a_star(graph, heuristic, 'A', 'Z')

# Test Case 6
print("\nTest Case 6:")

graph6 = {
    'A': {'B': 2},
    'B': {'A': 2},
    'C': {}
}

heuristic6 = {'A': 2, 'B': 1, 'C': 0}

a_star(graph6, heuristic6, 'A', 'C')

# Test Case 7
print("\nTest Case 7:")
a_star(graph, heuristic, 'A', 'H')

# Test Case 8
print("\nTest Case 8:")
a_star(graph, heuristic, 'X', 'H')
