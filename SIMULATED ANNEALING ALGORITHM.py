
import math
import random

def objective(x):
    return (x - 3) ** 2


def generate_neighbour(x):
    return x + random.uniform(-1, 1)


def simulated_annealing(objective, initial_state,
                        initial_temperature, cooling_rate,
                        minimum_temperature, maximum_iterations):

    current_state = initial_state
    current_cost = objective(current_state)

    best_state = current_state
    best_cost = current_cost

    temperature = initial_temperature

    for i in range(maximum_iterations):

        if temperature <= minimum_temperature:
            break

        candidate_state = generate_neighbour(current_state)
        candidate_cost = objective(candidate_state)

        delta = candidate_cost - current_cost

        if delta < 0:
            accept = True
        else:
            probability = math.exp(-delta / temperature)
            accept = random.random() < probability

        if accept:
            current_state = candidate_state
            current_cost = candidate_cost

            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost

        temperature *= cooling_rate

    return best_state, best_cost


# Test Case 1: Initial State at the Optimum
print("Test Case 1:")
random.seed(1)
x, cost = simulated_annealing(objective, 3, 100, 0.95, 0.01, 500)
print("Best State (x): {:.6f}".format(x))
print("Minimum Function Value: {:.8f}".format(cost))
# Expected: Low-cost value near the global minimum x = 3.


# Test Case 2: Initial State Below the Optimum
print("\nTest Case 2:")
random.seed(42)
x, cost = simulated_annealing(objective, -5, 100, 0.95, 0.01, 500)
print("Best State (x): {:.6f}".format(x))
print("Minimum Function Value: {:.8f}".format(cost))
# Expected: Best State approximately 2.997881.
# Minimum Function Value approximately 0.00000449.


# Test Case 3: Initial State Above the Optimum
print("\nTest Case 3:")
random.seed(7)
x, cost = simulated_annealing(objective, 9, 100, 0.95, 0.01, 500)
print("Best State (x): {:.6f}".format(x))
print("Minimum Function Value: {:.8f}".format(cost))
# Expected: Best State approximately 2.993599.
# Minimum Function Value approximately 0.00004097.


# Test Case 4: Low Initial Temperature
print("\nTest Case 4:")
random.seed(10)
x, cost = simulated_annealing(objective, 0, 1, 0.9, 0.01, 500)
print("Best State (x): {:.6f}".format(x))
print("Minimum Function Value: {:.8f}".format(cost))
# Expected: Best State approximately 2.995676.
# Minimum Function Value approximately 0.00001870.


# Test Case 5: Fast Cooling Schedule
print("\nTest Case 5:")
random.seed(21)
x, cost = simulated_annealing(objective, 10, 100, 0.5, 0.01, 100)
print("Best State (x): {:.6f}".format(x))
print("Minimum Function Value: {:.8f}".format(cost))
# Expected: Best State approximately 5.895203.
# Minimum Function Value approximately 8.38220061.
# The result should be a low-cost value near the global minimum x = 3.
