def desord(list):
    listInt=[]
    fin=len(list)-1
    for e in list:  
        listInt.append(list[fin])
        fin-=1
    
    return listInt
    # range(len(list)) exemple la taille de list est 5 donc range 0 1 2 3 4
    # range(len,fin, step) range(10,-1,-1) de 0,9 on commerce par le dernier et on décremente de 1


list=[1,2,3,4,5]
list2=desord(list)
print (list2)