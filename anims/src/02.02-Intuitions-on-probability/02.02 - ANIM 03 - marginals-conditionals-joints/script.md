# joints, conditionals, marginals

consideremos estos datos. que representan el número de personas que votaron por distintos partidos en distintas ciudades. 

esto **indica** una distribución de probabilidad **conjunta**. 

que este caso representa un aspecto de la realidad --> es empírica, es el resultado de contar cosas en el mundo real.

y estamos considerando una poblaciòn de **personas**, 

y describimos cada persona con dos características **DISCRETAS**

- el partido al que votó
- la ciudad en la que reside

y para cada posible combinación de valores tenemos tenemos una cuenta. P.ej. hubo 4 personas que en la ciudad 3 votaron al partido 2

con esto podríamos hacernos varias preguntas

- que proporción de personas votaron en total al partido X?
- qué proporción de personas votaron en la ciudad Y?
- por qué porcentaje gana el partido más votado?
- si yo me fijo solo en la ciudad Y, por qué porcentaje gana el partido más votado?

todas estas preguntas se responden en términos de probabilidades condicionales y marginales. y eso es lo que vamos a hablar en este video.

esta tabla no es una distribución de probabilidad, ni los valores están entre 0 y 1, ni todos suman 1.

convirtamos primeramente esta tabla en una distribución de probabilidad, es decir, hablemos de proporciones, no  de números absolutos, que es lo que tenemos

para ello, simplemente dividimos todos los valores por el total de personas que votaron, que son 324

ahora ya sí tenemos una distribución de probabilidad **conjunta**

llamemos X_p a la variable "partido político" y X_c a la variable ciudad.

con esto podemos responder a preguntas de valores **simultaneos** de ambas variables. por ejemplo:

- cuál es la probabilidad de que una persona haya votado al partido_1 **Y** sea de la ciudad_2 __circulo sobre el nùmero__

    P(X_p='party_1', X_c='city_3') = 0.142

    es decir, el 14.2 por ciento de la población es de la ciudad 3 y el partido 1

también podemos preguntar por el valor concreto de una sola variable. por ejemplo:

- qué porcentaje de la población votó al partido 2:

    P(X_p='party_2') = 0.376 = 0.123 + 0.241 + 0.012

o también

- cual es la probabilidad de que una persona sea de la ciudad_2
   
    P(X_c='city_2') = 0.513 = 0.142 + 0.241 + 0.031 + 0.099

Fíjate que para dar respuesta a estas dos preguntas, tenemos que sumar **todos** los valores de la otra variable. Es decir

    P(X_p=p) = \sum P(X_p=p , X_c=ci), con ci \in (city_1, city_2, city_3)

Cuando tenemos una distribución conjunta, PERO preguntamos por la probabilidad de una de las variables solamente, 

estamos MARGINALIZANDO (o sea, sumando sobre el resto de variables)

Fíjate que que P(X_p) obtenida de esta manera sí que es una distribución de probabilidad ya que

     P(X_p=party_1) + P(X_p=party_2) + P(X_p=party_3) + P(X_p=party_4)  = 1

Esta es la distribución de probabilidad **MARGINAL** para P(X_p)

e igual se podría hacer para P(X_c) ...  sumando en cada eje, tenemos ambas distribuciones de probabilidad marginales.

Restrinjamos ahora nuestra pregunta a una ciudad

- qué partido gana en ciudad_3?
- con qué porcentaje de votos?

fíjate que si tomamos sólo una columna (o una fila) **NO** tenemos una distribución de probaiblidad, ya que los elementos no suman 1.

para responder correctametne a la pregunta debemos de considerar **SOLO** los votos de la ciudad_3 y calcular las proporciones **UNICAMENTE** respecto a los votos de la ciudad_3

es decir, debemos de **NORMALIZAR**, 

P(X_p|X_c=ciudad_3) = ..../sum(....)

y así sí que tenemos una distribución de probabilidad.

Esto es la distribución de probabilidad **CONDICIONADA**

P(X_p|X_c) 