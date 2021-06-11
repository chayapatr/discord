n = int(input())
a = []
m = 0
for _ in range(n):
  x = int(input())
  a += [ x ]
  m = max(m,x)

for i in range(m):
  for j in range(n):
    for k in range(a[j]):
      if i + k == m - 1:
        print('/',end="")
      else:
        print(' ',end="")
    for k in range(a[j]):
      if i - k == m - a[j]:
        print('\\',end="")
      else:
        print(' ',end="")
  print("")