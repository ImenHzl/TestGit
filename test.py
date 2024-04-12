
def posp(list,target):
    element=-1
    compteur = 0
    for e in list:
        if e == target :
            element = compteur
        compteur+=1 
    return element

list = ["apple","mango","strawberry","pomegranate","melon"]
target = "mango"
position = posp(list, target)
print (position)

