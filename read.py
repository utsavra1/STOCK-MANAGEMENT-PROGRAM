def readfile():
    file = open('laptops.txt','r')
    laptop_id = 1
    mydict = {}
    for line in file:
        line = line.replace('\n','')
        mydict[laptop_id] = (line.split(','))
        laptop_id +=1
    file.close()
    return mydict
