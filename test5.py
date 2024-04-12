def listUniq(list):
    listSD=[]
    for e in list:
        if e not in listSD:
            listSD.append(e)
    return listSD


list=[4,6,4,8,10,8,6]
result= listUniq(list)
print (result)
            
    