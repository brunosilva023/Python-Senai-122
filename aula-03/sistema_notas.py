print('sistema de notas')
print('....'*8)

nome_aluno = input('Nome do aluno: ')
print()
n1_port = float(input('Nota portugues: '))
n2_mat = float(input('Nota matemática: '))
n3_ing = float(input('Nota inglês: '))
print()
media = (n1_port + n2_mat + n3_ing)/3
print()
print('Situação do aluno: ')
print()
aprovado = media >=7
reprovado = media <5
recuperacao = media >=5 and media <7
print()
print('Aprovado? - ', aprovado)
print('Aprovado? - ', reprovado)
print('Aprovado? - ', recuperacao)

