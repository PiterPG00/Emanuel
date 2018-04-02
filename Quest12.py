#PiterPG
sul = ["PARANÁ (PR)","RIO GRANDE DO SUL (RS)","SANTA CATARINA (SC)"]
norte = ["AMAZONAS (AM)","ACRE (AC)","RONDÔNIA (RO)","PARÁ (PA)","RORAIMA (RR)","AMAPÁ (AP)","TOCANTINS (TO)"]
nordeste = ["PARAIBA (PB)","RIO GRANDE DO NORTE (RN)","MARANHÃO (MA)","PIAUÍ (PI)","BAHIA (BH)","CEARÁ (CE)","PERNAMBUCO (PE)","ALAGOAS (AL)","SERGIPE (SE)"]
centro_oeste = ["MATO GROSSO (MT)","GOIÁS (GO)","MATO GROSSO DO SUL (MS)","DISTRITO FEDERAL (DF)"]
sudeste = ["SÃO PAULO (SP)","RIO DE JANEIRO (RJ)","ESPIRÍTO SANTO (ES)","MINAS GERAIS (MG)"]

rg = str(input("\nDigite a Região: "))

if (rg.upper() == "SUL"):
    print("\n\nESTADOS DA REGIÃO SUL!\n")
    for sul in sul:
        print(""+sul)

elif (rg.upper() == "NORTE"):
    print("\n\nESTADOS DA REGIÃO NORTE!\n")
    for norte in norte:
        print(""+norte)

elif (rg.upper() == "NORDESTE"):
    print("\n\nESTADOS DA REGIÃO NORDESTE!\n")
    for nordeste in nordeste:
        print(""+nordeste)

elif (rg.upper() == "CENTRO OESTE"):
    print("\n\nESTADOS DA REGIÃO CENTRO-OESTE!\n")
    for centro_oeste in centro_oeste:
        print(""+centro_oeste)

elif (rg.upper() == "SUDESTE"):
    print("\n\nESTADOS DA REGIÃO SUDESTE!\n")
    for sudeste in sudeste:
        print(""+sudeste)

else:
    print("\n\nESCOLHA APENAS AS REGIÕES:\n\nSUDESTE\nNORDESTE\nCENTRO-OESTE\nNORTE\nSUL")