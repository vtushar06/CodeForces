t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    freq = {}
    for i in range(n):
        freq[nums[i]] = freq.get(nums[i], 0) + 1
    for i in range(n):
        if freq[nums[i]] == 1:
            print(i + 1)
            break