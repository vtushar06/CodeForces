t=int(input())
for _ in range(t):
  n=int(input())
  s=input()
  count=0
  lis=[]
  for ch in s:
    if ch in lis:
      count+=1
    else:
      lis.append(ch)
      count+=2
  print(count)    