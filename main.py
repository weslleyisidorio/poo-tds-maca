import numpy as np
import time


def main():

    entrada = abrir_csv('apples_ts.csv')
    menu(entrada)
    

    
    

def abrir_csv(nome_arq:str):
    entrada = np.loadtxt(nome_arq, dtype=str, delimiter=',', skiprows=1)
    return entrada


def menu(dados):
    print('''------- MENU --------
1 - Listar media de preço por cidade: 
2 - Média de preço por ano: 
3 - :
0 - Sair 
          ''')
    try:
        escolha = int(input("Digite uma opção: "))
    except:
        print('Entrada inválida. Tente novamente:')
        main()

    if escolha == 1:
        cidade = input("Cidade: ").strip().capitalize()
        linha  = listar_cidade(cidade, dados)
        media = calcular_media_total(linha)
        print(f'Media: {media:.1f}')
    elif escolha == 2:
        cidade = input("Cidade: ").strip().capitalize()
        linha  = listar_cidade(cidade, dados)
        try:
            ano = int(input("Digite um ano: "))
        except:
            print("Entrada inválida!")
            main()

        mediaAnos = media_anos(ano, linha)
        print(f'Media de consumo de maças de {ano} em {cidade}: {mediaAnos:.1f}')

    elif escolha == 0:
        exit()


def listar_cidade(nome:str, dados):
    lin = [None]
    for linha in dados:
        if linha[0] == nome:
            lin = linha
    return lin
        

def calcular_media_total(dados):
    somatorio = 0
    for i in range(1, len(dados)-3):
        somatorio += float(dados[i])
    
    media = somatorio / (len(dados) - 4)

    return media

def calcular_media_ano(min, max, linha):
    somatorio = 0
    for i in range(min, max+1):
        somatorio += float(linha[i])
    print(somatorio)   
    media = somatorio / 12
    print(media)

    return media

def media_anos(ano, dados):
    anos = {2013: [1,12], 
            2014: [13,24],
            2015: [25,36],
            2016: [37,48],
            2017: [49,60],
            2018: [61,72],
            2019: [73,84]}
    min, max = anos[ano]
    print(min, max)    

    media = calcular_media_ano(min,max, dados)

    return media
    
    
if __name__ == "__main__":
    main()