n, k = input().split()
n = int(n)
k = int(k)
scores = [int(score) for score in input().split() if int(score) > 0]

if len(scores) != 0:
    if n == k:
        print(len(scores))
    elif k > len(scores):
        passed = scores[:k]    
        print(len(passed))
    else:    
        limit = scores[k-1]
        passed = scores[:k]
        for score in scores[k:]:
            if score == limit:
                passed.append(score)    
        print(len(passed))
else:
    print(0)

