a = [int(e) for e in input().split()]

product = 1
for x in a:
  product *= x

print(product)