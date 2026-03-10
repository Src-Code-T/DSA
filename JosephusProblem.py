def josephus(n, k):
    if n == 1:
        return 0

    return (josephus(n - 1, k) + k) % n

# Example usage:
n = int(input("Enter the number of people in the circle: "))
k = int(input("Enter the step count (k): "))
survivor = josephus(n, k)
print(f"The survivor is at position: {survivor}")