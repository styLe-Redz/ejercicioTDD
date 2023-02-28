from arregloMenor import encontrar_minimo

def test_encontrar_minimo():
    assert encontrar_minimo([1,2,3,4,5]) == 1
    assert encontrar_minimo([80, 30, 40, 27]) == 27
    assert encontrar_minimo([10, 15, 9, 3]) == 3
    
    