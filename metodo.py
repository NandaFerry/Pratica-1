import csv

def leitor_csv():
    lista = []
    with open("arquivo/entrada.csv") as csvfile:
        leitor = csv.reader(csvfile)
        for row in leitor:
            peso = int(row[0])
            beneficio = int(row[1])
            relacao = beneficio/peso
            lista.append({"Peso": peso, "Beneficio": beneficio, "Relacao": round(relacao, 3)})

    return lista

def ordena_lista():
    lista = leitor_csv()
    lista_ordenada = sorted(lista, key=lambda lista: lista['Relacao'])

    return lista_ordenada[::-1]

def construcao_gulosa():
    lista_ordenada = ordena_lista()
    capacidade = 0
    resultado = []
    for r in lista_ordenada:
        if capacidade > 100:
            return resultado
        resultado.append(r)
        capacidade += r["Peso"]




