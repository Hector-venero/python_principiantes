
print ("Buenas tardes usuario. \n\nEn este programa vamos a bucar los multiplos de 5 y 3 de un numero que nos indique ")
x = input ("Diga que numero quiere saber los multiplos \n" )
x=int(x)

multiplos3 = []
multiplos5 = []
diga= input("diga si quiere saber los multplos de 5 o de 3: \n")
diga=int(diga)

if diga ==3:
    for n in range(1, x+1, 1):
        if n%3 ==0:
            multiplos3.append(n)
    print("los multiplos de 3 para ese valor son: ")
    print(multiplos3)

if diga ==5:
    for n in range(1,x+1,1):
        if n%5 ==0:
            multiplos5.append(n)
    print ("los multiplos de 5 para ese valor son: ")
    print(multiplos5)        

print("\n\nFin del programa")

