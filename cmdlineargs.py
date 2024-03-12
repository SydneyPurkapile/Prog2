import sys

#print(sys.argv)

def main(args):
  if len(args) <= 0:
    print("Hello!")
    return
  print("Hello,", args[0])
  for arg in args:
    print(arg)

if __name__ == "__main__":
  main(sys.argv[1:])