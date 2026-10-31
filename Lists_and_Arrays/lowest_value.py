my_array = [7, 12, 9, 8, 3, 6]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i
        
print(f"Lowest value: {minVal}")