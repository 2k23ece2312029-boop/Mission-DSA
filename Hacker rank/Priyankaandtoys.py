def toys(w):
    """
    Calculates the minimum number of containers required for the given toy weights.

    Args:
        w: A list of integers representing the weights of the toys.

    Returns:
        An integer representing the minimum number of containers.
    """
    w.sort()  # Sort the weights in ascending order

    if not w:  # Handle the case of an empty list
        return 0

    containers = 1
    current_max_weight = w[0] + 4  # Max weight for the first container

    for i in range(1, len(w)):
        if w[i] > current_max_weight:
            containers += 1
            current_max_weight = w[i] + 4

    return containers

if __name__ == '__main__':
    # Example usage (as per HackerRank input format)
    n = int(input())  # Number of toys
    weights = list(map(int, input().split()))  # List of toy weights

    result = toys(weights)
    print(result)
