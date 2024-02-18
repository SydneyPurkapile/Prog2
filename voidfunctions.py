from calcfunctions import *
def doSomething():
  print("Hello World!")

def printNums():
  x = 0
  while x < 10:
    print("X:", x)
    x += 1
  pass
def main():
  doSomething()
  printNums()
  q, r = divmod2(5, 10)
  print(q, r)

if __name__ == "__main__":
  main()