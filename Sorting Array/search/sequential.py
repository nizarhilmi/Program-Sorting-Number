def Sequential(data, item, start, ke):

    pos = 0
    found = False
    
    while pos < len(data) and not found:
        if data[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos