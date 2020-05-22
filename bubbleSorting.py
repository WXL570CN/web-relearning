def bubbleSort(a):
  l = len(a)
  for i in range(l-1, -1, -1):
    for j in range(i):
      if(a[j] > a[j + 1]):
       a[j], a[j+1] = a[j+1], a[j]
    
a = [3,9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
bubbleSort(a)
print(a)