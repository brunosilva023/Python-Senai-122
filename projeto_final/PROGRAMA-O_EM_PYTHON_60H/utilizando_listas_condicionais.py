alunos = {
        'Ana':[10,9,8,5.5,3,7,10],
        'Fernanda':[1,2,3,6,5,2,7],
        'Leo':[10,10,10,10,10,10,10]
     }




NOTAS_ANA = alunos['Ana']
maior_nota_ana = max(NOTAS_ANA)
NOTAS_FERNANDA = alunos['Fernanda']
maior_nota_fernanda = max(NOTAS_FERNANDA)
NOTAS_LEO =alunos['Leo']
maior_nota_leo = max(NOTAS_LEO)

# print(f'MAIOR NOTA ANA - {maior_nota_ana}\nMAIOR NOTA FERNANDA - {maior_nota_fernanda}\nMAIOR NOTA LEO - {maior_nota_leo} ' )

media_ana = sum(alunos['Ana'])/len(alunos['Ana'])
media_fernanda = sum(alunos['Fernanda'])/len(alunos['Fernanda'])
media_leo = sum(alunos['Leo'])/len(alunos['Leo'])

medias = [media_ana, media_fernanda,media_leo]
media_total = sum(medias) / len(medias)



lista_nomes = ['Ana','Fernanda','Leo']
maior = max(medias)
indice = medias.index(maior)
# print(lista_nomes[indice], 'Maior Media', maior)


NOTAS_ANA.sort()
# print(f'mediana  ana- {NOTAS_ANA[3:4]}')
# print(f'amplitude  ana- {max(NOTAS_ANA) - min(NOTAS_ANA)}')
NOTAS_FERNANDA.sort()
# print(f'mediana  fernanda- {NOTAS_FERNANDA[3:4]}')
# print(f'amplitude  fernanda- {max(NOTAS_FERNANDA) - min(NOTAS_FERNANDA)}')
NOTAS_LEO.sort()
# print(f'mediana  leo - {NOTAS_LEO[3:4]}')
# print(f'amplitude  leo- {max(NOTAS_LEO) - min(NOTAS_LEO)}')

moda_ana = max(set(NOTAS_ANA), key=NOTAS_ANA.count)
# print('moda ANa', moda)

moda_fernanda = max(set(NOTAS_FERNANDA), key=NOTAS_FERNANDA.count)
# print('moda Fernanda', moda)

moda_leo = max(set(NOTAS_LEO), key=NOTAS_LEO.count)
# print('moda Leo', moda)



# média de notas soma() / len()
print('Sistema escolar')
print('1 - Media total | 2 - Media aluno | 3 moda mediana Amplitude |  4 -  Maior média | 5 Maior média p/ aluno')
escolha = input('Digite o que deseja visualizar')

if escolha == '1':
   print('MÉDIA GERAL', round(media_total,2))
elif escolha == '2':
   print('Média alunos:')
   print('Ana', media_ana)
   print('Fernanda', media_fernanda)
   print('Leo', media_leo)
elif escolha == '3':
   print('Moda |Mediana | Amplitude')
   print(f'mediana  ana- {NOTAS_ANA[3:4]}')
   print(f'amplitude  ana- {max(NOTAS_ANA) - min(NOTAS_ANA)}')
   print('moda ANa', moda_ana)
   print('--------------'*2)
   print(f'mediana  fernanda- {NOTAS_FERNANDA[3:4]}')
   print(f'amplitude  fernanda- {max(NOTAS_FERNANDA) - min(NOTAS_FERNANDA)}')
   print('moda Fernanda', moda_fernanda)
   print('--------------'*2)
   print(f'mediana  leo - {NOTAS_LEO[3:4]}')
   print(f'amplitude  leo- {max(NOTAS_LEO) - min(NOTAS_LEO)}')
   print('moda Leo', moda_leo)
elif escolha  == '4':
   print('Maiores notas dos alunos: ')   
   print(f'MAIOR NOTA ANA - {maior_nota_ana}\nMAIOR NOTA FERNANDA - {maior_nota_fernanda}\nMAIOR NOTA LEO - {maior_nota_leo} ' )
elif escolha == '5':
   print(lista_nomes[indice], 'Maior Media', maior)
else:
   print('Digite algo válido')   







