def digital_root(n):
    tempList =  ([int(number) for number in str(n)])
    while len(tempList) != 1:
        n = 0 
        for number in tempList:
            n += number
        tempList =  ([int(number) for number in str(n)])
    return n