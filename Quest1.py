#PiterPG
gasolina = float(input("Valor do Litro de Gasolina: "))
dinheiro = float(input("Dinheiro: "))

print("\nO Litro de Gasolina está R${:.2f} \n\
Você quer Abastecer R${:.2f} \n\
Vai dar {:.2f} Litros de Gasolina!".format(gasolina,dinheiro,dinheiro / gasolina))