list1 = [1,2,4]
list2 = [1,3,5]

# list1.extend(list2)
combined = list(set(list1.extend(list2)))

print(combined)