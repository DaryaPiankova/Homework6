massiv = [int(i) for i in input('Введите первый элемент прогрессии, разность и кол-во элементов: ').split()]
new_massiv=[]
for j in range(massiv[2]):
    new_massiv.append(massiv[0]+(j+1-1)*massiv[1])
print(new_massiv)
