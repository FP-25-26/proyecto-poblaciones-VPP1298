from collections import namedtuple
import csv
from matplotlib import *
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    registro_poblaciones = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            registro = RegistroPoblacion(pais, codigo, año, censo)
            registro_poblaciones.append(registro)
    return registro_poblaciones


def calcula_paises(poblaciones):
    paises = []
    for registro in poblaciones:
        paises.append(registro[0])
    paises = sorted(paises)
    return set(paises)


def filtra_por_pais(poblaciones, nombre_o_codigo):
    paises = []
    for registro in poblaciones:
        if registro[0] == nombre_o_codigo or registro[1] == nombre_o_codigo:
            paises.append((registro[2], registro[3]))
    return paises


def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    paises_habitantes = []
    for registro in poblaciones:
        if registro[2] == anyo and registro[0] in paises:
            paises_habitantes.append((registro[0], registro[3]))
    return paises_habitantes


def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes = []
    for registro in poblaciones:
        if registro[0] == nombre_o_codigo or registro[1] == nombre_o_codigo:
            lista_años.append(registro[2])
            lista_habitantes.append(registro[3])
    plt.title(nombre_o_codigo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = []
    lista_habitantes = []
    for registro in poblaciones:
        if registro[2] == anyo and registro[0] in paises:
            lista_paises.append(registro[0])
            lista_habitantes.append(registro[3])
    plt.title(str(paises) + " en el año " + str(anyo))
    plt.bar(lista_paises, lista_habitantes)
    plt.show()