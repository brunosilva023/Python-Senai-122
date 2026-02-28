import statistics


f = [1,2,3,6,5,5,7]
def moda(frequencia):
    moda= statistics.mode(frequencia)
    return moda


f = [1,2,3,4,5,5]
f.sort()
print(f)


def mediana(f):
    mediana = statistics.mediana(f)
    return mediana

x = [10,10,10,30,150,1000]

def media(f):
    media = statistics.mean(f)
    return media