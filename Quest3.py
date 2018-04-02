#PiterPG
divida = float(input("Valor da Divida: "))
atra = int(input("Dias Atrasados: "))
multa = float(input("Valor da Multa por Dia: "))

print("\nValor da Divida R${:.2f} \n\
Dias Atrasados [{}] \n\
Multa de R${:.2f} \n\
Valor Final: R${:.2f}".format(divida,atra,multa,(multa * atra) + divida))