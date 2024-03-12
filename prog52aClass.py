from socket import AddressFamily, AddressInfo


class Shape:

  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0
    self._perim = 0

  def calculate(self):
    self._area = self.length * self.width
    self._perim = self.length*2 + self.width*2

  def getArea(self):
    return self._area

  def getPerim(self):
    return self._perim

def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter Width: "))
  shape = Shape(len, wid)
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerim())

if __name__ == "__main__":
  main()