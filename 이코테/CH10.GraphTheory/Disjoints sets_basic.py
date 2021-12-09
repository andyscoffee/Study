# 서로소 집합

def find_parents(parent, x):
  if parent[x] != x:
    parent[x] = find_parents(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parents(parent, a)
  b = find_parents(parent, b)
  if a> b:
    parent[a] = b
  else:
    parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

for i in range(1, v+1):
  print(find_parents(parent, i), end = ' ')
print()

for i in range(1, v+1):
  print(parent[i], end = ' ')
