def isComposite(n):
  if n < 4:
    return False
  for i in range(2, n):
    if n % i == 0:
      return True
  return False
n=int(input())
for x in range(4,n):
  y =n-x 
  if isComposite(x) and isComposite(y):
    print(x, y)
    break