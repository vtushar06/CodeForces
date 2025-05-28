t=int(input())
def fashionable_array_even(a):
    l, r = 0, len(a) - 1
    count = 0
    
    while l < r:
        if (a[l] + a[r]) % 2 == 0:
            return count
        elif a[l] % 2 != 0:
            l += 1
            count += 1
        elif a[r] % 2 != 0:
            r -= 1
            count += 1
            
    return count
def fashionable_array_odd(a):
    l, r = 0, len(a) - 1
    count = 0
    
    while l < r:
        if (a[l] + a[r]) % 2 == 0:
            return count
        elif a[l] % 2 == 0:
            l += 1
            count += 1
        elif a[r] % 2 == 0:
            r -= 1
            count += 1
            
    return count
  
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  a.sort()
  print(min(fashionable_array_odd(a), fashionable_array_even(a)))