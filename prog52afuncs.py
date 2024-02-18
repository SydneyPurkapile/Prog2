def calcArea(len, wid):
  return len * wid

def calcPerim(len, wid):
  return len * 2 + wid * 2

def areaPerim(len, wid):
  area = calcArea(len, wid)
  perim = calcPerim(len, wid)
  return area, perim

def main():
  length = int(input("Enter the Length: "))
  width = int(input("Enter the WIdth: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerimeter: {p}")


if __name__ == "__main__":
  main()