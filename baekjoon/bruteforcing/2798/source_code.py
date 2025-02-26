import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for selected_cards in combinations(cards, 3):
    total = sum(selected_cards)
    if total <= m:
        result = max(result, total)

print(result)