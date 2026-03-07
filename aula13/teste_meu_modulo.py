# test_meu_modulo

from modulos import imc

def test_modulo():
    assert imc(80,1.80) ==  24.69
    assert imc(60,1.80) ==  18.52
    assert imc(50,1.80) ==  15.43
    assert imc(100,1.80)==  30.86

