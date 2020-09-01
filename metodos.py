import csv
import random

#Método para ler a entrada do arquivo csv
def leitor_csv():
    lista = []
    with open("arquivo/entrada.csv") as csvfile:
        leitor = csv.reader(csvfile)
        for row in leitor:
            peso = int(row[0])
            beneficio = int(row[1])
            relacao = beneficio/peso
            #Aqui estamos criando um dicionario para guardar os dados da entrada
            lista.append({"Peso": peso, "Beneficio": beneficio, "Relacao": round(relacao, 3)})

    return lista

#Método para ordernar a lista da maior relação para a menor
def ordena_lista():
    lista = leitor_csv()
    lista_ordenada = sorted(lista, key=lambda lista: lista['Relacao'])

    #Aqui estamos invertendo a lista para que as maiores relações sejam as primeiras
    return lista_ordenada[::-1]

#Método com o algoritmo da construção gulosa
def construcao_gulosa():
    lista_ordenada = ordena_lista()
    capacidade = 0
    resultado = []
    for r in lista_ordenada:
        #Enquanto a capacidade for menor que 100 iremos adicionar um item no resultado
        if capacidade > 100:
            return resultado
        resultado.append(r)
        capacidade += r["Peso"]

#Método com o algoritmo da construção aleatoria
def construcao_aleatoria():
    lista = leitor_csv()
    capacidade = 0
    resultado = []

    while capacidade <= 100: #Enquanto houver capacidade
        item = random.choice(lista) #Escolhe aleatoriamente o item a ser inserido
        resultado.append(item)
        capacidade += item["Peso"]
        x = 0
        for i in lista:
            if item == i:
                del (lista[x]) #Remove o item escolhido da lista para que não seja escolhido novamente
            x += 1

    return resultado
