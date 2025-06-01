t=int(input())
for _ in range(t):
  a,b=map(int,input().split())
  ans=abs(a-b)
  for i in range(a,b):
    minimise=(i-a)+(b-i)
    ans=min(minimise,ans)
  print(ans)  