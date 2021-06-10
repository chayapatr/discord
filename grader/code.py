import multiprocessing
import sys

def runner():
  sys.stdin = open(0)
  a=int(input())
  b=int(input())
  print(a+b)

timeout = 1

if __name__ == '__main__':
    p = multiprocessing.Process(target=runner, name="runner")
    p.start()

    p.join(timeout)

    if p.is_alive():
      print("Terminate  - Exceed Limit Time")
      p.terminate()
      p.join()
  