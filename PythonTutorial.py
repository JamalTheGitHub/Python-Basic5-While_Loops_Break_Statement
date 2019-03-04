a = [6,5,4,3,1,-1,-4,-5,-7,-8]
total = 0
i = 0

# Solution 1

# while True and i < len(a):
    
#   if a[i] < 0:
#     total += a[i]

#   i += 1

# print(total)


##################################

# Solution 2

# for i in a:

#   if i < 0:
#     total += i

# print(total) 


##################################

# Solution 3

# j = len(a) - 1

# while a[j] < 0:
#   if a[j] > 0:
#     break

#   total += a[j]
#   j -= 1

# print(total)


#################################