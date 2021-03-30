def exchangeSort(data):
    batas=len(data)
    i=0
    j=1
    while i!=batas-1:
        while j!=batas:
            if data[i]>data[j]:
                data[i],data[j]=data[j],data[i]
            i+=1
            j+=1
            if j==batas:
                i=0
                j=1
                batas-=1
        
def exchange(data,x):
    for i in range(0,x):
        for j in range(0,x):
            y=i+1
            for j in range(y,x):
                if data[i]>data[j]:
                    data[i],data[j]=data[j],data[i]
                    print(data)
                    break
            else:
                break
