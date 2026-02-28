# verificar a valor_hora
def verificar_valor_hora(carga,salario):
    return salario / carga


# verificar quantidade de horas extras

def quantidade_extra(valor_extra,valor_hora):

    return valor_extra * valor_hora

# calculo do valor da hora extra total
def hora_extra_receber(quantidade, hora_extra):
    return quantidade * hora_extra

# somar com o salario
def salario_bruto (salario,hora_extra_receber):
    return salario + hora_extra_receber

# verificar os descontos  vt, vr
def descontos (salario_bruto,vt,vr):
    return salario_bruto - (vt+vr)

# liquido e o bruto

def salario_liquido (salario_receber):
    return salario_receber


def sistema_rh():
    while True:
        salario = float(input("Salario R$: "))
        carga = 220
        print("Verifique o salario a receber ")
        valor_hora = verificar_valor_hora(carga,salario)
        print("Valor hora R$: ",(round, valor_hora,2))
        print('****'*10)
        extra_50 =  quantidade_extra(1.5,valor_hora)
        extra_100 =  quantidade_extra(2.0,valor_hora)
        print("Extra 50% ",round (extra_50,2))
        print("Extra 100% ",round( extra_100,2))
        print('****'*10)
        quantidade_50 = float(input("quantidade de extra realizada 50% :"))
        quantidade_100 = float(input("quantidade de extra realizada 100% :"))
        hora_receber_50 = hora_extra_receber(quantidade_50,extra_50)
        hora_receber_100 = hora_extra_receber(quantidade_100,extra_100)
        print(f'''
                Hora extra 50% - R$ : {hora_receber_50}
                Hora extra 100% - R$ : {hora_receber_100}


''')
        print('****'*10)
        hora_extra_total = hora_receber_50+hora_receber_100
        salario_b = salario_bruto(salario,hora_extra_receber)
        print("Salario Bruto: R$: " ,round(salario_b,2))

        print("Descontos: " )

        salario_liqui =  descontos(salario_b,1000.0, 750.0)

        print("Salario Liquido : R$: " , salario_liqui)

        print("Salario a receber - R$ : ",salario_liquido(salario_liqui))

sistema_rh()