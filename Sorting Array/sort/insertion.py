import time

def insertion(data,n): 

    if n<=1: 
        return data
  
    insertion(data,n-1)
    last = data[n-1] 
    j = n-2
      

    while (j>=0 and data[j]>last): 
        data[j+1] = data[j] 
        j = j-1
  
    data[j+1]=last 
      


