import timer
import fileHandler
import binAlgorithms
import cleanup
import sys


def consoleResult(t, capacity, items, data):
  context = "Test Case {}".format(t + 1)
  for d in data:
    context = "{} {}: {}, {}ms.".format(context, d[0], len(d[2]), d[1].time() * 1000)
    
  print context 

def writeLog(log):
  content = "test,items,capacity,ff_bins,ffd_bins,bf_bins,ff_ms,ffd_ms,bf_ms\n"
  for row in log:
    content += "{},{},{},{},{},{},{},{},{}\n".format(row["t"] + 1, len(row["items"]), row["capacity"], len(row["ff"][2]), len(row["ffd"][2]), len(row["bf"][2]), row["ff"][1].time() * 1000, row["ffd"][1].time() * 1000, row["bf"][1].time() * 1000)

  fileHandler.writeCsv("log.csv", content)

def main(path):
  results = []
  #path = "./input/bin2.txt"
  #path = "./input/random_test.txt"
  tests = fileHandler.parseFile(path)
  for i in range(0, len(tests[0:30000])):
    test = tests[i]
    capacity = test.capacity
    items = test.items

    #FF
    ff = ["First Fit", timer.Timer()]
    ff.append(binAlgorithms.firstFit(capacity, items))
    ff[1].end()

    #BF
    bf = ["Best Fit", timer.Timer()]
    bf.append(binAlgorithms.bestFit(capacity, items))
    bf[1].end()

    #FFD
    ffd = ["First Fit Decreasing", timer.Timer()]
    ffd.append(binAlgorithms.firstFitDecreasing(capacity, items))
    ffd[1].end()
   
    consoleResult(i, capacity, items, [ff, ffd, bf])
    results.append({"t": i, "capacity": capacity, "items": items, "ff": ff, "ffd": ffd, "bf": bf})

  writeLog(results)
  cleanup.pyc()

if __name__ == "__main__":
  path = "bin.txt"
  if len(sys.argv) > 1:
    path = sys.argv[1]
  main(path)
