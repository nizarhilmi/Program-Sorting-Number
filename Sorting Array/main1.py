import time
from sort.insertion import insertion
from search.binary import binarySearch
from sort.bubble import bubble
from sort.merge import merge
from sort.merge import merge_sort
from sort.selections import selection
from sort.shell import shellSort
from search.sequential import Sequential
from sort.exchange import exchangeSort
from sort.exchange import exchange


def main():
  ops = True
  data = []
  print("\n\n__________________________\n")
  print("Input Data yang Ingin di 'Sort' atau di 'Search' dalam Menu ")
  print("contoh: 2 1 4 3 5")
  temp = input("masukkan bilangan: ")
  temp = temp.split()
  data = list(map(int, temp))
  print("\n__________________________\n\n")

  while(ops):


    print("_______________________________________________________")
    print("|\t\t\tMENU                          |")
    print("+_____________________________________________________+")
    print("|\t1. bubble sort                                |")
    print("|\t2. exchange sort                              |")
    print("|\t3. selection sort                             |")
    print("|\t4. insertion sort                             |")
    print("|\t5. merge sort                                 |")
    print("|\t6. shell sort                                 |")
    print("|\t7. sequential sort                            |")
    print("|\t8. binary search                              |")
    print("|\t9. exit                                       |")
    print("+_____________________________________________________+\n")
    choice = int(input("masukkan pilihan: "))

    if choice == 1:

     print("\n\n__________________________\n")
     print("data sebelum diurutkan")
     print(*data)

     start = time.time()
     result = iter(bubble(data))
     print("data sesudah diurutkan")

     print(*result)
     print("waktu yang dibutuhkan:")
     print(time.time()-start,' seconds.')
     print("\n\n___________________________\n")

    elif choice == 2:

      print("\n\n__________________________\n")
      print("data sebelum diurutkan")
      print(*data)

      start = time.time()
      n = len(data)
      exchangeSort(data) 

      print("data sesudah diurutkan")
      result = iter(data)

      print(*result)
      print("waktu yang dibutuhkan:")
      print(time.time()-start,' seconds.')
      print("\n_________________________\n\n")

    elif choice == 3:

      print("\n\n________________________\n")
      print("data sebelum diurutkan")
      print(*data)

      start = time.time()
      n = len(data)
      selection(data) 

      print("data sesudah diurutkan")
      result = iter(data)

      print(*result)
      print("waktu yang dibutuhkan:")
      print(time.time()-start,' seconds.')
      print("\n_________________________\n\n")

    elif choice == 4:

      print("\n\n________________________\n")
      print("data sebelum diurutkan")
      print(*data)

      start = time.time()
      n = len(data)
      insertion(data, n) 

      print("data sesudah diurutkan")
      result = iter(data)

      print(*result)
      print("waktu yang dibutuhkan:")
      print(time.time()-start,' seconds.')
      print("\n__________________________\n\n")

    elif choice == 5:

      print("\n\n_________________________\n")
      print("data sebelum diurutkan")
      print(*data)
      start = time.time()
      fin = iter(merge_sort(data))

      print("data sesudah diurutkan")
      print(*fin)
      print("waktu yang dibutuhkan:")
      print(time.time()-start,' seconds.')
      print("\n__________________________\n\n")

    elif choice == 6:

      print("\n\n_________________________\n")
      print("data sebelum diurutkan")
      print(*data)

      start = time.time()
      n = len(data)
      shellSort(data, n) 

      print("data sesudah diurutkan")
      result = iter(data)

      print(*result)
      print("waktu yang dibutuhkan:")
      print(time.time()-start,' seconds.')
      print("\n__________________________\n\n")

    elif choice == 7:

      print("\n\n_________________________\n")
      print("note: jika ingin menggunakan feature ini dengan benar urutkan terlebih dahulu!!\n")
      print("data sudah diurutkan")
      print(*data)
      key = int(input("nomer yang dicari: "))


      start = time.time()
      index = Sequential(data, 0, len(data), key)
      if index == 0:
        print("{} tidak ditemukan." .format(key))
        print("waktu yang dibutuhkan:")
        print(time.time()-start,' seconds.')
      else:
        print("{} ditemukan" .format(key))
        print("waktu yang dibutuhkan:")
        print(time.time()-start,' seconds.')
      print("\n__________________________\n\n")

    elif choice == 8:

      print("\n\n_________________________\n")
      print("note: jika ingin menggunakan feature ini dengan benar urutkan terlebih dahulu!!\n")
      print("data sudah diurutkan")
      print(*data)
      key = int(input("nomer yang dicari: "))


      start = time.time()
      index = binarySearch(data, 0, len(data), key)
      if index < 0:
        print("{} tidak ditemukan." .format(key))
        print("waktu yang dibutuhkan:")
        print(time.time()-start,' seconds.')
      else:
        print("{} ditemukan" .format(key))
        print("waktu yang dibutuhkan:")
        print(time.time()-start,' seconds.')
      print("\n__________________________\n\n")

    elif choice == 9:

      ops = False

    else:
      print("\n\n__________________________\n")
      print("input yang anda masukan salah ndan jangan spaneng keep santuy!!")
      print("\n_____________________________\n\n")
      
      
  print("\n\n_______________________________\n\n")
  print("Have a nice day :) !!")
  print("\n\n_______________________________\n\n")



if __name__=="__main__":
  main()