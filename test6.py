def rotGauche(list):
    listNew=[]
    i=1
    for i in range(len(list)):
        listNew.append(list[i])
    listNew.append(list[0])
    return listNew

list=[1,2,3,4]
result= rotGauche(list)
print (result)
