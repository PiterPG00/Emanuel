#PiterPG
kminicio = int(input("Km Inicial: "))
kmfinal = int(input("Km Final: "))
gasolina = float(input("Litros de Gasolina Gasto: "))

print("\nVocê andou {} Km \n\
O Carro fez {:.1f} Km por Litro!".format(kmfinal - kminicio,(kmfinal - kminicio) / gasolina))