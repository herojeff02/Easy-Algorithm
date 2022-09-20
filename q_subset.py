def sum_of_subset(curr, index, rem):
    x[index] = 1
    print_list = []
    print(curr, index, rem)
    for i in range(0, index + 1):
        if x[i] == 1:
            print_list.append(set[i])
    print(print_list)
    if curr + set[index] < target_sum:
        sum_of_subset(curr + set[index], index + 1, rem - set[index])
    if curr + rem - set[index] >= target_sum >= curr + set[index + 1]:
        x[index] = 0
        sum_of_subset(curr, index + 1, rem - set[index])


set = [3, 34, 4, 12, 5, 2]
set.sort()
target_sum = 9
x = [0 for i in range(len(set)+1)]
sum_of_subset(0, 0, sum(set))
