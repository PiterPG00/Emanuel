#PiterPG
import time
saldo = 1000.00
while True:
    print("""
0 - SAIR
1 - SAQUE
2 - DEPÓSITO
3 - SALDO""")

    esco = int(input("\nEscolha: "))

    if (esco == 0):
        print("\nNós do Banco ,Agradecemos sua Preferência!")
        print("Dono: Pedro Henrique (PiterPG)")
        print("Volte Sempre!")
        exit()

    elif (esco == 1):
        saque = float(input("\nVocê tem R${:.2f}\nDeseja Sacar Quanto?\nR$".format(saldo)))
        if (saldo >= saque):
            saldo -= saque
            time.sleep(1.5)
            print("\nVocê Efetuou o Saque de R${:.2f}!\nVocê tem R${:.2f} Na Conta!".format(saque,saldo))
            time.sleep(1.5)
        elif (saldo < saque):
            time.sleep(1.5)
            print("\nSaldo Insuficiente para Completar esta Transação!")
            time.sleep(1.5)
    elif (esco == 2):
        inserir = float(input("Saldo a ser Depositado: "))
        
        if (inserir > 0):
            time.sleep(1.5)
            saldo += inserir
            print("\nDepósito de R${:.2f} Feito Com Sucesso!".format(inserir))
            print("\nVocê tem R${:.2f} Na Conta Agora!".format(saldo))
       
        elif (inserir <= 0):
            time.sleep(1.5)
            print("Saldo Invalido Para Depositar!")

    elif (esco == 3):
        time.sleep(1.5)
        print("\nVocê tem R${:.2f}!".format(saldo))
        print("\nNós do Banco ,Agradecemos sua Preferência!")
        print("Dono: Pedro Henrique (PiterPG)")
        time.sleep(1.5)

    else:
        print("\nSelecione Apenas os Certos!")