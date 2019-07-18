num_raw = int(input())
stones = list(input())

count = 0
if stones.count("R") > 1 or stones.count("B") > 1 or stones.count("G") > 1:
    for idx, stone in enumerate(stones):
        if idx == 0:
            if stone == stones[idx + 1]:
                count += 1
        elif idx == len(stones) - 1:
            pass
        else:
            if stone == stones[idx + 1]:
                count += 1

print(count)
