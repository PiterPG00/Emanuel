#PiterPG
nome = str(input("\nDigite seu Nome: "))
sexo = str(input("Qual seu Sexo: "))

if (sexo.upper() == "MASCULINO"):
    print("\nIlmo Sr. {}".format(nome))

elif (sexo.upper() == "FEMININO"):
    print("\nIlma Sra {}".format(nome))

else:
    print("\nSelecione Feminino ou Masculino!")