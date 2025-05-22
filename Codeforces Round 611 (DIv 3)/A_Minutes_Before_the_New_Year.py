t=int(input())
for _ in range(t):
  h,m=map(int,input().split())
  total_minutes=h*60+m
  left_minutes=1440-total_minutes
  print(left_minutes)