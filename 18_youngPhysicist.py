n_dim = int(input())

allowed_chars = [str(i) for i in range(-101, 101)]
sum_vectors1 = 0
sum_vectors2 = 0
sum_vectors3 = 0

for i in range(n_dim):
    vector = input().split(" ")
    vector[:] = [int(char) for char in vector if char in allowed_chars]
    sum_vectors1 += vector[0]
    sum_vectors2 += vector[1]
    sum_vectors3 += vector[2]

if sum_vectors1 == 0 and sum_vectors2 == 0 and sum_vectors3 == 0:
    print("YES")
else:
    print("NO")