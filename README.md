# Caminata_aleatoria
# Por Jose Maria Cardenas Ramirez

# En este proyecto implementamos un algoritmo para simular la ruta que podría segur un borracho
# dado que es igual de probable que vaya de derecha a izquierda, de adelante hacia atrás. Desarrollamos 
# 4 escenarios: 

# En el primero da 10 pasos, 
# en el segundo da 100 pasos, 
# el tercero 1000 y en el cuarto
# 10,000 pasos. 

# Para cada escenario corremos 100 simulaciones.  
# Calculamos tambien la distancia media que alcanza a recorrer desde el punto de partida (0,0)
# hasta el ultimo paso que dió. Asi como el punto máximo y mínimo.

# Dividimos el algoritmo en 3 clases:

# borracho
#   class borracho : Almacena el nombre del borracho.
#   class borrachoTradicional : Hereda de "borracho". 
#           Contiene el metodo "camina" : regresa el siguiente paso que dará.

# coordenada
#   class Coordenada : COntiene el metodo mover, que  suma las cordenadas actuales con las siguientes.
#           El metodo "distancia" calcula la distancia entre el punto actual  con  el  origen.

# campo
#   class Campo : Crea un diccionario que guarda las coordenadas.
#           contiene el metodo mover_borracho. Regresa la coordenada actual del borracho.


# Las tres clases se utilizan en el archivo principal "camino aleatorio.py"
# Utilizamos la libreria Bokeh.plotting para mostrar las rutas.

# El trabajo está diseñado para poder  cambiar las probabilidades de las direcciones en 
# la clase borracho, en el metodo "camina" basta con cambiar los pesos.

# Este trabajo forma parte de la serie de Ejercicios de la Escuela de Data Science de Platzi.
