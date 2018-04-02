#PiterPG
com1 = float(input("Cômodo 1 - Comprimento: "))
lar1 = float(input("Cômodo 1 - Largura: "))
com2 = float(input("\nCômodo 2 - Comprimento: "))
lar2 = float(input("Cômodo 2 - Largura: "))
com3 = float(input("\nCômodo 3 - Comprimento: "))
lar3 = float(input("Cômodo 3 - Largura: "))
com4 = float(input("\nCômodo 4 - Comprimento: "))
lar4 = float(input("Cômodo 4 - Largura: "))

fim1,fim2,fim3,fim4 = com1*lar1,com2*lar2,com3*lar3,com4*lar4

print("\nCômodo 1 é {:.2f} M² \n\
Cômodo 2 é {:.2f} M² \n\
Cômodo 3 é {:.2f} M² \n\
Cômodo 4 é {:.2f} M² \n\
Cômodos Juntos é {:.2f} M²".format(fim1,fim2,fim3,fim4,fim1+fim2+fim3+fim4))
