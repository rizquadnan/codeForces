num_input = int(input())
x_value = 0
for i in range(num_input):
    statement = list(input())
    if '+' in statement:
        x_value += 1
    elif '-' in statement:
        x_value -= 1

print(x_value)