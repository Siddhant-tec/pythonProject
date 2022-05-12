from itertools import combinations, chain
items = list(map(int, input().rstrip().split()))
x = list(chain.from_iterable(combinations(items, r) for r in range(len(items)+1)))
y = [list(i) for i in x]
print(y)
