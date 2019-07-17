matrix = []
tag = {}
for i in range(5):
    line = list(input())
    line = [element for element in line if element != " "]
    if "1" in line:
        tag['row'] = i
        tag['col'] = line.index("1")
    matrix.append(line)

print(abs(2 - tag["row"]) + abs(2 - tag["col"]))