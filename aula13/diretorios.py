import os
import shutil

import os
import shutil

print(os.listdir('C:/Users/Aluno/Downloads/nova_pasta_2/'))

shutil.copytree('novo_nome2', 'copia_2')
shutil.rmtree('teste2')

#diretório

with open('n', 'w') as arq:
    os.mkdir('teste2')
    
##read o arquivo    

with open('teste2/teste_6', 'w') as novo:
    os.mkdir('novo_arq')

#faz a leitura do arquivo

with open('teste4.txt', 'r') as arq:
    conteudo =  arq.read()
    print(conteudo)


with open('teste4.txt', 'r') as arq:
    conteudo =  arq.read()
    print(conteudo)    

os.rename('teste','novo_nome')
os.rename('novo_arq','novo_nome2')

#acessar o diretório e verificar o que tem nele
with os.scandir('C:/Users/Aluno/Downloads/nova_pasta_2/teste2') as dados:
         x = [x.name for x in dados] 
         print(x)
        
def verificar():
    with os.scandir('C:/Users/Aluno/Downloads/nova_pasta_2/teste2')  as dados:
        x  =  [i.name for i in dados]
        
        print(x)
        if 'teste_6' in x :
                print('existe')
        else:
            print('não encontrou')              