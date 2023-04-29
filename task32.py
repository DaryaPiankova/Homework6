diapazon=[int(i) for i in input('Введите диапазон: ').split()]
massiv = [int(i) for i in input().split()]
print([j for j in range(len(massiv)) if massiv[j]>= diapazon[0] and massiv[j]<=diapazon[1]])
