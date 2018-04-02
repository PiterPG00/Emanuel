#PiterPG
dolar = float(input("\nCotação do Dólar: "))
money = float(input("Dinheiro em Real: "))
print("\nCotação do Dólar tá U${:.2f} \n\
Valor de U$ (Dólar) Para R$ (Real) \nÉ R${:.2f}".format(dolar,money / dolar))