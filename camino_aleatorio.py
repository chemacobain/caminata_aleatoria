from borracho import borrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata,1))
    x_ilum = []
    y_ilum = []
    # Grafica la caminata aleatoria
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        a = campo.coordenadas_borrachos[borracho].x
        b = campo.coordenadas_borrachos[borracho].y
        x_ilum.append(a)
        y_ilum.append(b)
    graficar(x_ilum, y_ilum)

    return distancias

def graficar(x,y):
    grafica = figure(title='camino aleatorio', x_axis_label='pasos',y_axis_label='distancia' )
    grafica.line(x,y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata,  numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        dist_media = round((sum(distancias)/len(distancias)),4)
        dist_max = max(distancias)
        dist_min = min(distancias)
        distancias_media_por_caminata.append(dist_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de:{pasos}')
        print(f'Media = {dist_media}')
        print(f'Max = {dist_max}')
        print(f'Max = {dist_min}')

    

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata,numero_de_intentos,borrachoTradicional)

