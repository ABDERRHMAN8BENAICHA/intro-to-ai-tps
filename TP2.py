my_classeur = {"negatifs":[],"positifs":[]}

def trier(classeur,value):
    if(value > 0):
        classeur["positifs"].append(value)
    else :
        classeur["negatifs"].append(value)
    return classeur
trier(my_classeur,10)
trier(my_classeur,-30)
print("negatifs is : ",my_classeur["negatifs"])
print("positifs is : ",my_classeur["positifs"])