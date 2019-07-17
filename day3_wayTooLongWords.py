n = int(input())
words = []
for i in range(n):
    words.append(input())

for word in words:
    if len(word) > 10:
        first = word[0]
        last = word[-1]
        between = str(len(word[1:-1]))
        output = first + between + last
        print(output)
    else:
        print(word)


