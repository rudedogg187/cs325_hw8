from random import randint
import fileHandler


path = "./input/random_test.txt"

test_min = 5
test_max = 5

items_min = 100
items_max = 200

item_min = 400
item_max = 1000

content = ""

test_count = randint(test_min, test_max)

content += "{}\n".format(str(test_count))
#print "Test Count:  {}".format(test_count)

for i in range(0, test_count):
  item_count = randint(items_min, items_max)


  capacity = 0 
  items = ""
  for j in range(0, item_count):
    item = randint(item_min, item_max)
    if item > capacity:
      capacity = item

    items += "{} ".format(str(item))


  capacity = randint(capacity, capacity * 1)
 
  content += "{}\n".format(capacity)
  #print "  Capacity:  {}".format(capacity)

  content += "{}\n".format(str(item_count))
  #print "  Item Count:  {}".format(item_count)

  content += "{}\n".format(items)
  #print "  Items: {}".format(items)

content += "\n\n"
#print "---"
#print content 


fileHandler.writeFile(path, content)
  




