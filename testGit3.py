def fusList(list1, list2):
    listFus= []
    i=0
    for e in list1 :
        listFus.append(e+list2[i])
        i+=1
    return listFus

list1=['a','b','c']
list2=['1','2','3']
result=fusList(list1,list2)
print(result)