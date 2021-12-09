# 서로소 판별

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
cyle = False

for i in range(e):
  a, b = map(int, input().split())
  if find_parents(parent, a) == find_parents(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클 발생")