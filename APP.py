from Robo import robo
from Acessos import lst_ambientes, lst_robos_producao, lst_robos_homologa

cod_robo = ""
while cod_robo != "0":
    #CONSULTA AMBIENTES 
    i = 1
    while i < len(lst_ambientes):
        print(lst_ambientes[i][1],"-", lst_ambientes[i][0])
        i = i + 1

    print("")
    cod_ambiente = int(input("Digite o código escolhido: "))

    print("")
    print("Robôs:")

    if cod_ambiente == 1:
    #CONSULTA LISTA DE ROBÔS 
        i = 1
        while i < len(lst_robos_producao):
            print(lst_robos_producao[i][2],"-", lst_robos_producao[i][0])
            i = i + 1

    if cod_ambiente == 2:
    #CONSULTA LISTA DE ROBÔS 
        i = 1
        while i < len(lst_robos_homologa):
            print(lst_robos_homologa[i][2],"-", lst_robos_homologa[i][0])
            i = i + 1

    print("0 - Voltar")
    print("")
    cod_robo = int(input("Digite o código escolhido: "))

robo(cod_ambiente, cod_robo)

