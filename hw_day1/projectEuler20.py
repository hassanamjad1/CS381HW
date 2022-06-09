# n = 10
# product = 1
def getNum(n):
  if n == 1:
    return 1
  return n * getNum(n-1)
  # return n

def getSum(n):
  sum = 0 
  while n > 0 :
    m = n%10
    sum = sum+m
    n = n//10
  return sum

product = getNum(100)
SUM = getSum(product)
print(SUM)


