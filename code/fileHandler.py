import csv


class Test:
  def __init__(self, test, capacity, items):
    self.test = test
    self.capacity = capacity
    self.items = items



def parseFile(path):
  tests = []
  with open(path, "r") as f:
    rows = f.read().strip().replace("\r", "").split("\n")

  t = 0
  test_count = int(rows.pop(0))
  
  while t < test_count:
    capacity = int(rows[t * 3])
    item_count = int(rows[t * 3 + 1])
    items = [int(item) for item in rows[t * 3 + 2].strip().split(" ")]
    test = Test(t, capacity, items)
    tests.append(test)
    t += 1

  return tests


def writeFile(path, content):
  with open(path, "w") as f:
    f.write(content)


def writeCsv(path, content):
  with open(path, "w") as f:
    csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting= csv.QUOTE_MINIMAL)

    for row in content.split('\n'):
      if len(row.split(",")) > 1:
        csv_writer.writerow(row.split(","))


   


def main():
  path = "./input/bin2.txt"
  path = "./input/random_test.txt"
  tests = parseFile(path)
  
  for test in tests:
    print test.test
    print test.capacity
    print test.items
    print


if __name__ == "__main__":
  main()

