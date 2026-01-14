lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# l = len(lst)

# for y in range(0, l):
#     if lst[y] % 3 == 0 and lst[y] > 15:
#         print(lst[y])

result = [x for x in lst if x > 15 and x % 3 == 0]

print(result)
