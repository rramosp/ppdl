# Probability basics

Vamos a repasar en este video y en los siguientes algunas nociones básicas de probabilidad.

[0.06] Recuerda que una distribución de probabilidad asigna números entre cero y uno a los objectos que estamos considerando y la podemos representar con una función.

[0.16] Ahora, si los objetos que estamos considerando los podemos describir con cualquier valor dentro de un cierto rango, entonces tenemos una distribución de probabilidad continua. Y ahora vamos a ver algunos ejemplso. 

[0.29] Y si los describimos con valores (o símbolos o nombres de cosas, lugares, categorias,...) de un conjunto limitado, entonces tenemos una distribución discreta.

(partir la pizara en dos, izda, y derecha, la izda para discreta, la dcha para continua)

[0.41] Por ejemplo, si los objetos que estamos considerando son "profesiones de personas" entonces tendremos una distribución de probabilidad discreta, y tendremos un valor de probabilidad para cada profesión, que pueden ser muchas, pero es un conjunto limitado.

(show P(engineer)=0.01, P(accountant)=0.03, P(teacher)=0.02, etc.)

[0.58] O también tendremos una distribución de probabilidad discreta si los objetos que estamos considerando son poblaciones de ciudades (ya que tendremos un número limitado de ciudades), 

[1.16] o poblaciones por rangos de edades (p.ej. con 5 rangos de edades, entre 0-10,10-30,30-50, 60-80, 80-),

[1.24] o distintas alternativas para una decisión (salgo a correr, salgo al cine, me quedo en casa), 

[1.33] o el número de mensajes de correo que me llega cada día (me pueden mardar 1,2,15,20,100, pero no 13.68)

[1.54] Y recuerda siempre que una distribución de probabilidad puede tener muchas interpretaciones: una estimación de la realidad, una cuantificación de nuestro conocimiento, los resultados de un censo, etc.

[2.18] Pero por ejemplo, si los objetos que estamos considerando son las alturas de las personas de una población entonces tenemos una distribución continua, ya que dentro de dos valores extremos cualquier altura es posible. Podemos tener personas de que midan 165cm, 177cm , 168.23cm, hasta de 168.4512cm si pudiéramos medir con esa precisión.

[2.53] O si los objetos que estamos considerando son los tiempos que transcurren entre dos mensajes de correo consecutivos también tenemos una distribución continua. Dependiendo de la precisión podríamos tener valores de 3.5segs, 1min 15.234segs, 1 day y 3mins, etc. 

[5.10] La función que asigna probabilidades a objetos en el caso discreto se denomina 

[5.20] Probability Mass Function (o PMF) y en el 

[5.25] caso continuo Probability Density Function (o PDF). 

[5.31] La convención es que cuando estamos en un caso continuo hablamos de densidad (que es una proporción, como cantidad de probabilidad por tiempo -si es el ejemplo del tiempo entre mensajes-, o cantidad de probabilidad por cm si es la altura de las personas), y en el caso discreto hablamos de masa.

[5.53] Una PDF se suele representar por un gráfico de una función continua. Y una PMF por un gráfico de barras (poner ejemplos)

[6.06] Y por supuesto la condición de que todas las posibles probabilidades tienen que sumar uno se expresa como una [6.20] sumatoria en el caso discreto, y [6.25] como una integral en el caso continuo.

[6.30] Al conjunto de objetos que estamos considerando se le suele denominar **VARIABLE ALEATORIA** y la distribución de probabilidad se **describe** por medio de la PMF o PDF, que es la asignación de probabilidades (números entre cero y uno) a valores de la variable aleatoria.

[6.57] Para una distribución continua podríamos preguntarnos también cual es la probabilidad de que la variable aleatoria fuera menor que cierto valor. 

[7.06] P.ej. P(tiempo entre mensajes<1min). 

[7.22] A esta función, que asigna una probabilidad a un intervalo entre menos infinito (o el mínimo posible) a un valor de nuestra variable aleatoria se le denomina CDF, y es una función que a veces es muy útil como veremos en los notebooks.

(pintar fórmula cdf)

[7.42] Y una sutileza, pequeña pero muy importante, para finalizar este video. La probabilidad que asigna una PDF en una distribución continua es **infinitesimal**. 

[8.05] En un caso continuo, no tiene sentido preguntar, por ejemplo, P(t=2.32secs), porque es imposible tener precisión infinita en la medición. Podemos preguntar P(t$\in$[2.32, 2.33]) que sería la integral entre 2.32 y 2.33 de la PDF.

De hecho preguntar por la probabilidad de un valor concreto, sería equivalente a reducir ese intervalo hasta hacerlo cero (es decir, un punto) que en realidad nos daría una probabilidad cero.

Una consecuencia de esto es que la PDF de cualquier valor puntual pueda ser >1, aunque la integral de cualquier intervalo siempre sea <1.