import statistics

def calcular_media(notas):
    return sum(notas) / len(notas)


def calcular_moda(notas):
    try:
        return statistics.multimode(notas)
    except statistics.StatisticsError:
        return "Não há moda"
    

def calcular_desvio_padrao(notas):
    if len(notas) < 2:
        return 0.0
    return statistics.stdev(notas)

def obter_extremos(notas):
    return min(notas), max(notas)


def exibir_relatorio(notas):

    if not notas:
        print("Nenhuma nota cadastrada.")
        return
    media = calcular_media(notas)
    moda = calcular_moda(notas)
    desvio = calcular_desvio_padrao(notas)
    minima, maxima = obter_extremos(notas)

    print("\n--- ESTATÍSTICAS DAS NOTAS ---")
    print()

    print(f'''
    "Média Geral:      {[round(media,2)]}")
    "Moda:             {(moda)}")
    "Desvio Padrão:    {[round(desvio,2)]}")
    "Menor Nota:       {[round(minima,2)]}")
    "Maior Nota:       {[round(maxima,2)]}")
    
 ''')
if __name__ == "__main__":
    notas_alunos = [7.5, 8.0, 6.5, 9.0, 7.5, 10.0, 5.5, 8.0, 7.5, 4.0]
    exibir_relatorio(notas_alunos)
