n, k = map(int, input().split())
parti = list(map(int, input().split()))
eligible = [y for y in parti if y <= 5 - k]
print(len(eligible) // 3)