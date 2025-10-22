from collections import namedtuple
from poblacion import *

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def test_lee_poblaciones(ruta_fichero):
    return lee_poblaciones(ruta_fichero)

def test_calcula_paises(poblaciones):
    return calcula_paises(poblaciones)

def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    return filtra_por_pais(poblaciones, nombre_o_codigo)

def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    return filtra_por_paises_y_anyo(poblaciones, anyo, paises)

def test_muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    return muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)

def test_muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    return muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

if __name__ == "__main__":
    poblaciones = test_lee_poblaciones("data/population.csv")
    #print(test_lee_poblaciones("data/population.csv"))
    #print(test_calcula_paises(poblaciones))
    #print(test_filtra_por_pais(poblaciones, "Spain"))
    #print(test_filtra_por_paises_y_anyo(poblaciones, 1961, ["Spain", "Zimbabwe"]))
    #print(test_muestra_evolucion_poblacion(poblaciones, 'Spain'))
    print(test_muestra_comparativa_paises_anyo(poblaciones, 2000, ["Spain", "Arab World", "Zimbabwe"]))
    