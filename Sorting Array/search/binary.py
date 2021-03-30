import time

def binarySearch(data, start, end, key):

  if not start < end:
    return -1

  mid = (start + end)//2
  if data[mid] < key:
    return binarySearch(data, mid + 1, end, key)
  elif data[mid] > key:
    return binarySearch(data, start, mid, key)
  else:
    return mid


