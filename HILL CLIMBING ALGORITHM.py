def hill_climbing(graph, values, initial_state):

    # Check initial state
    if initial_state not in graph or initial_state not in values:
        print("Invalid initial state:", initial_state)
        return

    current = initial_state
    path = [current]

    while graph[current]:

        best_neighbour = current

        # Find the neighbour with highest value
        for neighbour in graph[current]:

            if values[neighbour] > values[best_neighbour]:
                best_neighbour = neighbour

        # Stop if no better neighbour exists
        if best_neighbour == current:
            break

        # Move to the better neighbour
        current = best_neighbour
        path.append(current)

    print("Path:", " -> ".join(path))
    print("Final State:", current)
    print("Evaluation Value:", values[current])


# Test Case 1
print("\nTest Case 1: Normal Hill Climbing")

graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

values1 = {
    'A': 2, 'B': 4, 'C': 5,
    'D': 7, 'E': 6, 'F': 8, 'G': 9
}

hill_climbing(graph1, values1, 'A')


# Test Case 2
print("\nTest Case 2: Initial State is Best")

graph2 = {
    'A': ['B', 'C'],
    'B': [], 'C': []
}

values2 = {'A': 10, 'B': 5, 'C': 7}

hill_climbing(graph2, values2, 'A')


# Test Case 3
print("\nTest Case 3: Single Neighbour")

graph3 = {'A': ['B'], 'B': []}
values3 = {'A': 3, 'B': 8}

hill_climbing(graph3, values3, 'A')


# Test Case 4
print("\nTest Case 4: Local Maximum")

graph4 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [], 'E': []
}

values4 = {
    'A': 3, 'B': 8, 'C': 5,
    'D': 6, 'E': 10
}

hill_climbing(graph4, values4, 'A')


# Test Case 5
print("\nTest Case 5: Plateau")

graph5 = {
    'A': ['B', 'C'],
    'B': [], 'C': []
}

values5 = {'A': 5, 'B': 5, 'C': 5}

hill_climbing(graph5, values5, 'A')


# Test Case 6
print("\nTest Case 6: Lower Neighbour Values")

graph6 = {
    'A': ['B', 'C'],
    'B': [], 'C': []
}

values6 = {'A': 9, 'B': 6, 'C': 4}

hill_climbing(graph6, values6, 'A')


# Test Case 7
print("\nTest Case 7: Multiple Neighbours")

graph7 = {
    'A': ['B', 'C', 'D'],
    'B': [], 'C': [], 'D': []
}

values7 = {'A': 2, 'B': 5, 'C': 9, 'D': 7}

hill_climbing(graph7, values7, 'A')


# Test Case 8
print("\nTest Case 8: No Neighbours")

graph8 = {'A': []}
values8 = {'A': 5}

hill_climbing(graph8, values8, 'A')


# Test Case 9
print("\nTest Case 9: Invalid Initial State")

graph9 = {'A': ['B'], 'B': []}
values9 = {'A': 3, 'B': 8}

hill_climbing(graph9, values9, 'X')


# Test Case 10
print("\nTest Case 10: Local vs Global Maximum")

graph10 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [], 'E': []
}

values10 = {
    'A': 2, 'B': 8, 'C': 4,
    'D': 6, 'E': 10
}

hill_climbing(graph10, values10, 'A')

