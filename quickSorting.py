def quickSort(a, l, r):
  i = l
  j = r
  if(i >= j):
    return
  key = a[i]
  while i < j:
    while (i < j) and (a[j] >= key) :
      j -= 1
    a[i], a[j] = a[j], a[i]
    while (i < j) and (a[i] <= key):
      i += 1
    a[i], a[j] = a[j], a[i]

  quickSort(a, l, i - 1)
  quickSort(a, j + 1, r)

a = [3,9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
quickSort(a, 0, len(a) - 1)
print(a)