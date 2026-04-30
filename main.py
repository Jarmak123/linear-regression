from itertools import accumulate

import matplotlib as mpl
import math

from numpy.f2py.auxfuncs import throw_error


def get_data(name_of_file):
    result = []
    x = []
    y = []
    with open(name_of_file, "r") as f:
        data = f.readlines()

    for i in data:
        x.append(float(i))
        y.append(float(i))

    result.append(x)
    result.append(y)
    return result

def calculate_srednia(data:list):
    acumulate = 0
    for i in data:
        acumulate += i

    return acumulate/len(data)

def calculate_odchylenie_standardowe(data:list,srednia_z_data):
    new_data = []
    acumulate = 0
    for i in data:
        new_data.append((i-srednia_z_data)**2)

    for i in new_data:
        acumulate += i

    return round(math.sqrt(acumulate/(len(data)-1)),2)

def korelacja_pearsona(data_x:list, data_y:list):
    if len(data_x) != len(data_y): throw_error("Lista X musi pokrywać liste Y!")

    acumulate_xy = 0
    acumulate_x = 0
    acumulate_y = 0
    for i in range(0, len(data_x)): acumulate_xy += data_x[i]*data_y[i]
    for i in range(0, len(data_x)): acumulate_x += data_x[i]
    for i in range(0, len(data_y)): acumulate_y += data_y[i]

    acumulate_x_potega = 0
    acumulate_y_potega = 0
    for i in range(0, len(data_x)): acumulate_x_potega += data_x[i]**2
    for i in range(0, len(data_x)): acumulate_y_potega += data_y[i]**2

    gora = len(data_x)*acumulate_xy-acumulate_x*acumulate_y
    dol = math.sqrt((len(data_x)*acumulate_x_potega-acumulate_x**2)*(len(data_y)*acumulate_y_potega-acumulate_y**2))
    result = gora/dol


    return round(result,2)

def main():
    # data=get_data("data.txt")
    # print(data)
    x = [1,2,3,4,5]
    y = [4,6,9,11,18]

    srednia_x = calculate_srednia(x)
    srednia_y = calculate_srednia(y)

    odchylenie_x = calculate_odchylenie_standardowe(x,srednia_x)
    odchylenie_y = calculate_odchylenie_standardowe(y,srednia_y)

    korelacja = korelacja_pearsona(x,y)

    print(srednia_x)
    print(srednia_y)
    print(odchylenie_x)
    print(odchylenie_y)
    print(korelacja)

    # obliczenie wspolczynnika

    if korelacja > 0:
        print("korelacja dodatnia")
    elif korelacja < 0:
        print("korelacja ujemna")
    else:
        print("korelacja nie występuje")

    



main()