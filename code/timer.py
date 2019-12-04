import timeit


class Timer:
  def __init__(self):
    self.s = 0
    self.e = -1
    self.start()

  def start(self):
    self.s = timeit.default_timer()
    self.e = timeit.default_timer()
    return self.time()

  def end(self):
    self.e = timeit.default_timer()
    return self.time()

  def time(self):
    return self.e - self.s
  


def test():
  t = Timer()
  t.start()
  t.end()
  print t.time()


if __name__ == "__main__":
  test()

    
