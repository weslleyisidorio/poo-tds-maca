import numpy as np


def main():

    entrada = abrir_csv('apples_ts.csv')
    menu(entrada)
    

    
    

def abrir_csv(nome_arq:str):
    entrada = np.loadtxt(nome_arq, dtype=str, delimiter=',', skiprows=1)
    return entrada


def menu(dados):
    print('''------- MENU --------
1 - Listar por cidade: 
2 - Média por ano: 
3 - Maior consumidor:
0 - Sair 
          ''')
    try:
        escolha = int(input("Digite uma opção: "))
    except:
        print('Entrada inválida. Tente novamente:')
        main()

    if escolha == 1:
        cidade = input("Cidade: ").strip().capitalize()
        listar_cidade(cidade, dados)
    elif escolha == 0:
        exit()


def listar_cidade(nome:str, dados):
    lin = [None]
    for linha in dados:
        if linha[0] == nome:
            lin = linha
            media = calcular_media(lin)
    return lin
        

def calcular_media(dados):
    somatorio = 0
    for i in range(1, len(dados)-3):
        somatorio += float(dados[i])
    
    media = somatorio / (len(dados) - 4)

    return media

def media(ano, dados):
    anos = {2013: [1,12], 
            2014: [13,24],
            2015: [25,36],
            2016: [37,48],
            2017: [49,60],
            2018: [61,72],
            2019: [73,84]}
    

    
    


if __name__ == "__main__":
    main()