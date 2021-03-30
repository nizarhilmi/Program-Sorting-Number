import time

def bubble(data):
    x = 0
    for i in range(len(data)-1):
        if data[i] > data[i + 1]:
            data[i],data[i + 1] = data[i + 1],data[i]
            x += 1
    if x == 0:
        return data
    else:
        return bubble(data)
           
