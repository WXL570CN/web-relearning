# 快速排序
# 将一组数据分成两个部分，是其中一部分中任意数据都要大于另一部分中的数据
def quickSort(a, l, r):
  i, j = l, r
  if(i >= j):
    return
  key = a[i]
  while(i < j):
    while(i < j and a[j] >= key):
      j -= 1
    a[i], a[j] = a[j], a[i]
    while(i < j and a[i] <= key):
      i += 1
    a[i], a[j] = a[j], a[i]

  quickSort(a, l, i - 1)
  quickSort(a, j + 1, r)

a = [3,9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
quickSort(a, 0, len(a) - 1)
print(a)

# 冒泡排序
# 每一次遍历都得到一个最大的数
def bubbleSort(b):
  l_b = len(b) - 1
  for i in range(l_b, -1, -1):
    for j in range(i):
      if(b[j] > b[j+1]):
        b[j], b[j+1] = b[j+1], b[j]

b = [3, 9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
bubbleSort(b)
print(b)

# 插入排序
# 遍历，将后面的数据依次插入到前面的数据中，使之始终有序
def insertSort(c):
  l_c = len(c)
  for i in range(1, l_c):
    j = i
    while(j > 0 and c[j] < c[j-1]):
      c[j], c[j-1] = c[j-1], c[j]
      j -= 1

c = [3, 9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
insertSort(c)
print(c)

# 归并排序
# 将一组数据不断等分，直到分成的每一小部分都有序，再将其合并为一组有序的数据
def merged(left, right):
  merged = []
  i, j = 0, 0
  l_l, l_r = len(left), len(right)
  while(i < l_l and j < l_r):
    if(left[i] <= right[j]):
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged

def main(d):
  l_d = len(d)
  if(l_d <= 1):
    return d
  mid = l_d // 2
  
  left = main(d[:mid])
  right = main(d[mid:])

  return merged(left, right)

d = [3, 9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
d1 = main(d)
print(d1)

