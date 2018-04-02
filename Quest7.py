#PiterPG
nota1 = float(input("\n1° Nota: "))
nota2 = float(input("2° Nota: "))
nota3 = float(input("3° Nota: "))
nota4 = float(input("4° Nota: "))
final = (nota1 + nota2 + nota3 + nota4) / 4

if (final >= 6):
    print("\nNota Final: [{:.2f}]\n\
APROVADO!".format(final))

else:
    print("\nNota Final: [{:.2f}]\n\
Faltou [{:.2f}] Para Você Passar! \n\
REPROVADO!".format(final,6 - final))