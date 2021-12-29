# 국영수 (핵심 유형)

n = int(input())
student = []
for i in range(n):
  student.append(input().split())
  
student.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in student:
  print(i[0])
