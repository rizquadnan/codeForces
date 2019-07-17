num = int(input())
solutions = []
num_problems = 0

for i in range(num):
    solution = list(str(input()))
    solution = [char for char in solution if char != ' ']
    if solution.count("1") >= 2:
        num_problems += 1

print(num_problems)
