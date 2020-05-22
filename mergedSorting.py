def merged(leftArr, rightArr):
  merged = []
  i, j = 0, 0
  lenL, lenR = len(leftArr), len(rightArr)
  while (i < lenL and j < lenR):
    if(leftArr[i] <= rightArr[j]):
      merged.append(leftArr[i])
      i += 1
    else:
      merged.append(rightArr[j])
      j += 1
  merged.extend(leftArr[i:])
  merged.extend(rightArr[j:])
  return merged

def main(a):
  lenA = len(a)
  if(lenA <= 1):
    return a
  midIndex = lenA // 2
  left = main(a[:midIndex])
  right = main(a[midIndex:])
  return merged(left, right)

a = [3,9, 2, 8, 7, 4, 5, 1, 10, 6, 0]
a1 = main(a)
print(a1)