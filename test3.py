def listPair(list):

    listNbrPair=[]
    for e in list:
        if(type(e)== int):
            if e % 2 == 0:
                listNbrPair.append(e)
        
    return listNbrPair

list=[1,3,4,6,7, 8 ,'a']
listReslt=listPair(list)
print(listReslt)