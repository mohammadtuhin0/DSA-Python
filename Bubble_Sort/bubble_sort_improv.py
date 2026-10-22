mylist = [7, 12, 9, 11, 3]
n = len(mylist)
comparison_count = 0
swap_count = 0

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        comparison_count += 1
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swap_count += 1
            swapped = True
    if not swapped:
        break
print(mylist)
print(f"Comparison : {comparison_count}")
print(f"Swapped : {swap_count}")