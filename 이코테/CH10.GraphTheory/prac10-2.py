# 도시 분할 계획 

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
edges = []
res = 0
maximum = 0
for i in range(1, v+1):
  parent[i] = i
cyle = False

for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parents(parent, a) == find_parents(parent, b):
    union_parent(parent, a, b)
    res += cost
    maximum = cost

print(res - maximum)