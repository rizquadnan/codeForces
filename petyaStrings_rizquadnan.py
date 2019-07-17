str1 = list(str(input()).lower())
str2 = list(str(input()).lower())

count1 = 0
count2 = 0
for char1, char2 in  zip(str1, str2):
    if char1 > char2:
        count1 += 1
        break
    elif char1 < char2:
        count2 += 1
        break
    else:
        pass

if count1 > count2:
    print(1)
elif count1 < count2:
    print(-1)
else:
    print(0)
