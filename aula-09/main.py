
import Aluno.Downloads.aula9.calculos_matematicos as cl
from Aluno.Downloads.aula9.jogo import advinha
import Aluno.Downloads.aula9.visualizacao

# C:\Users\Aluno\Downloads\aula9\calculos_matematicos.py
# C:\Users\Aluno\Downloads\aula9\jogo.py
# C:\Users\Aluno\Downloads\aula9\visualizacao.py


def main():
    f =  [1,2,3,5,5,6]
    moda_1  = cl.moda(f)
    print(moda_1)


    mediana_1 =  cl.mediana(f) 
    print(mediana_1)


    media_1 =  cl.media(f)
    print(media_1)


    print('****' * 15)



    t =  int(input('Número: '))
    resultado = advinha(t)
    print(resultado)



    print('****' * 15)



    mostrar_1 =  aula9.visualizacao.imagem1()
    print(mostrar_1)
    mostrar_2 =  aula9.visualizacao.imagem2()
    print(mostrar_2)
    mostrar_3 =  aula9.visualizacao.visualizar('text')
    print(mostrar_3)


main()