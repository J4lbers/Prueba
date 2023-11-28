
def separ_list(a):
    ejemplo=[1,2,3,4,5,6,7,8,9]
    list.sort()
    pares = []
    impares = []
    for i in list:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
separ_list()