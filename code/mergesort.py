###################
# HUGHES, JOSHU L
# CS325 OSU
# MERGE SORT - REFACTORED FROM ASSIGNMENT 1
# ASSIGNMENT 8
# 01 DEC 2019
##################

def mergeSort(lst, p, r, rev = False):
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  if p < r:
    q = (p + r) / 2

    mergeSort(lst, p, q, rev)
    mergeSort(lst, q + 1, r, rev)
    merge(lst, p, q, r, rev)

def merge(lst, p, q, r, rev):
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  n_1 = q - p + 1
  n_2 = r - q

  llst = lst[:n_1]
  rlst = lst[len(lst) - n_2:]

  for i in range(0, n_1):
    llst[i] = lst[p + i]

  for j in range(0, n_2):
    rlst[j] = lst[q + 1 + j]

  i = 0
  j = 0

  k = p

  x = 0 

  while i < n_1 and j < n_2:
    x += 1
    l_val = int(llst[i])
    r_val = int(rlst[j])

    if l_val <= r_val and rev == False:
      lst[k] = llst[i]
      i += 1

    elif l_val >= r_val and rev != False:
      lst[k] = llst[i]
      i += 1

    else:
      lst[k] = rlst[j]
      j += 1

    k += 1

  while i < n_1:
    lst[k] = llst[i]
    i += 1
    k += 1

  while j < n_2:
    lst[k] = rlst[j]
    j += 1
    k += 1




def mergeSortIndex(lst, p, r, idx, rev = False):
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  if p < r:
    q = (p + r) / 2

    mergeSortIndex(lst, p, q, idx, rev)
    mergeSortIndex(lst, q + 1, r, idx, rev)
    mergeIndex(lst, p, q, r, idx, rev)

def mergeIndex(lst, p, q, r, idx, rev):
  '''REF PSUDO CODE FROM TEXT (INTO TO ALGORTHIMS V3)'''
  n_1 = q - p + 1
  n_2 = r - q

  llst = lst[:n_1]
  rlst = lst[len(lst) - n_2:]

  for i in range(0, n_1):
    llst[i] = lst[p + i]

  for j in range(0, n_2):
    rlst[j] = lst[q + 1 + j]

  i = 0
  j = 0

  k = p

  x = 0 

  while i < n_1 and j < n_2:
    x += 1
    l_val = int(llst[i][idx])
    r_val = int(rlst[j][idx])

    if l_val <= r_val and rev == False:
      lst[k] = llst[i]
      i += 1

    elif l_val >= r_val and rev != False:
      lst[k] = llst[i]
      i += 1

    else:
      lst[k] = rlst[j]
      j += 1

    k += 1

  while i < n_1:
    lst[k] = llst[i]
    i += 1
    k += 1

  while j < n_2:
    lst[k] = rlst[j]
    j += 1
    k += 1

def main():

  lst = [1, 10, 8, 9]
  print lst
  mergeSort(lst, 0, len(lst) -1, 1)
  print lst


if __name__ == "__main__":
  main()

