num_stops = int(input())
min_capacity = -float("inf")
capacity = 0
for i in range(num_stops):
    traffic = input().split()
    traffic = [int(char) for char in traffic if char != " "]
    if i == 0:
        capacity = traffic[1]
        min_capacity = capacity
    elif i == num_stops - 1:
        pass
    else:
        capacity -= traffic[0]
        capacity += traffic[1]
        if capacity > min_capacity:
            min_capacity = capacity

print(min_capacity)
