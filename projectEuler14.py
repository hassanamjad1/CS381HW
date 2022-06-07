# n = 1000
longestCount = 1
result = 1
for n in range(1000000):
  num = n
  count = 0
  while n > 1:
    if n%2 == 0:
      n = n/2
    else:
      n = (3*n) + 1
    count += 1
  if count > longestCount:
    longestCount = count
    result = num
print('number with longest chain under 1M : ',result)

    
    
    


