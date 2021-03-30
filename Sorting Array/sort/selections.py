def selection(data):

   for i in range(len(data)):

       minPosition = i

       for j in range(i+1, len(data)):
           if data[minPosition] > data[j]:
               minPosition = j
                       
       temp = data[i]
       data[i] = data[minPosition]
       data[minPosition] = temp

   return data
    
