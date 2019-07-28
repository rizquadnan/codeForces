num_group = int(input())
groups = list(input())
groups = [int(num_people) for num_people in groups if num_people != " "]

import math
num_taxi = 0
count_one = groups.count(1)
count_two = groups.count(2)
count_three =  groups.count(3)
count_four = groups.count(4)

num_taxi += count_four

if count_one != 0 and count_three != 0:
    if count_one >= count_three:
        num_taxi += count_three
        count_one -= count_three
    else:
        num_taxi += count_one
        count_three -= count_one
        num_taxi += count_three
        count_one = 0
elif count_one == 0 and count_three != 0:
    num_taxi += count_three

if count_one != 0 and count_two != 0:
    sum_one_two = count_one + count_two * 2
    if sum_one_two <= 4:
        num_taxi += 1
    else:
        num_taxi += math.ceil(sum_one_two/4)
elif count_one == 0 and count_two != 0:
    num_taxi += math.ceil(count_two/2)
elif count_one != 0 and count_two == 0:
    num_taxi += math.ceil(count_one/4)

print(num_taxi)
