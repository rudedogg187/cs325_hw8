import timer
import fileHandler
import cleanup
import mergesort


def fit(bins, capacity, item):
  packed = 0
  for bin in bins:
    if bin[0] + item <= capacity:
      bin[1].append(item)
      bin[0] += item
      packed = 1
      break

  if not packed:
    bins.append([item,[item]])

  return bins


def firstFit(capacity, items):
  bins = []
  for i in range(0, len(items)):
    item = items[i]

    fit(bins, capacity, item)

  return bins



def firstFitDecreasing(capacity, items):
  mergesort.mergeSort(items, 0, len(items) -1, 1)
  return firstFit(capacity, items) 



def bestFit(capacity, items):
  bins = []
  for i in range(0, len(items)):
    item = items[i]

    mergesort.mergeSortIndex(bins, 0, len(bins) -1, 0, 1)

    fit(bins, capacity, item)

  return bins


def consoleResult(time, capacity, bins):      
  print "Time:\t\t{}".format(time) 
  print "Capacity:\t{}".format(capacity)
  print "Bins:\t\t{}".format(len(bins))
  '''
  for bin in bins:
    print "\t", bin
  '''
  print "---------------------------------"


def ff():
  print "FF"
  path = "./bin2.txt"
  #path = "./random_test.txt"
  tests = fileHandler.parseFile(path)

  for test in tests[0: 100]:
    capacity = test.capacity
    items = test.items
    bins = []
    ff_timer = timer.Timer()
    firstFit(bins, capacity, items)
    time = ff_timer.end()
    consoleResult(time, capacity, bins)


def ffd():
  print "FFD"
  path = "./bin2.txt"
  #path = "./random_test.txt"
  tests = fileHandler.parseFile(path)
  
  for test in tests[0: 100]:
    capacity = test.capacity
    items = test.items

    bins = []
    ffd_timer = timer.Timer()
    firstFitDecreasing(bins, capacity, items)
    time = ffd_timer.end()
    consoleResult(time, capacity, bins)


def bf():
  print "BF"
  path = "./bin2.txt"
  #path = "./random_test.txt"
  tests = fileHandler.parseFile(path)

  for test in tests[0: 100]:
    capacity = test.capacity
    items = test.items

    bins = []
    bf_timer = timer.Timer()
    bestFit(bins, capacity, items)
    time = bf_timer.end()
    consoleResult(time, capacity, bins)

if __name__ == "__main__":
  bf()

  cleanup.pyc()


