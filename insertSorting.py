def insertSort(a):
  l = len(a)
  for i in range(1, l):
    j =  i
    while(a[j] < a[j - 1] and j > 0):
      a[j], a[j-1] = a[j-1], a[j]
      j -= 1

a = [3,9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
insertSort(a)
print(a)