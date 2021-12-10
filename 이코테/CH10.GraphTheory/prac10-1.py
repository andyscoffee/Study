# 팀 결성

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
  do, a, b = map(int, input().split())
  if do == 0:
    union_parent(parent, a, b)
  elif do == 1:
    if find_parents(parent, a) == find_parents(parent, b):
      print('Yes')
    else:
      print('No')