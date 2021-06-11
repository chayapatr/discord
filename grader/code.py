import multiprocessing
import sys
import time

def runner():
  sys.stdin = open(0)
  n = int(input())
  p = int(input())
  a = 0
  for x in range(1,n+1):
    a += x**p
  print(a)

if __name__ == '__main__':
  p = multiprocessing.Process(target=runner)
  start = time.time()
  p.start()
  while (time.time() - start) <= 1 and p.is_alive():
    pass
  if p.is_alive():
    print("Terminate  - Exceed Limit Time")
    p.terminate()
    p.join()
