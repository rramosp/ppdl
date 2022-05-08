[0:0] las nociones de distribuciones conjuntas, marginales y condicionales son análogas a lo que acabamos de ver, cuando alguna de las variables (o todas) son continuas.

simplemente tenemos que tener en cuenta dos cosas:

[0:16] - que tendremos que sustituir las sumatorias por integrales
[0:20] - que tenemos que tener en cuenta el rango de soporte de cada variable para realizar las integrales en los intervalos correctos. Por ejemplo, una longitud de algún objeto no tendrá valores negativos ni muy grandes, por tanto su distribución de probabilidad debería de estar limitada a los valores válidos.

[0:41] Supongamos que nos dan la siguiente distribución conjunta de dos variables contínuas. En el notebook a continuación vamos a ver en concreto de dónde puede salir una distribución parecida y cómo manejarla.

Tenemos dos variables que describen el largo y el ancho de ciertas especies de microorganismos, o de bichitos.

El intervalo válido de valores para la longitud es entre 0 y 5mm, y para el ancho entre 0 y 1mm. Es decir, los bichitos que estamos considerando no exceden en ningún caso el rango de esos valores. 

Y estamos viendo los contornos de la densidad de probabilidad. Las zonas más oscuras son las que presentan más frecuencia de bichitos con los valores correspondientes de ancho y largo. 

[1:30] Por ejemplo los bichitos más frecuentes son los que tienen aproximadamente 0.5 de ancho y 1.9 de alto. 

[1:36] estos otros también son bastante frecuentes. 

[1:39] y según nos vamos a zonas más claras, la probabilidad de encontrar bichitos con estas dimensiones se hace más pequeña

[1:51] Lo que tenemos representado en este gráfico es una distribución de probabilidad conjunta

$$P(l,w)$$

[2:00] Las condiciones que garantizan que tenemos una distribución de probabilidad son

[2:06] que la suma de todos los posibles valores sea 1

[2:12] y que la suma probabilidades de cualquier región esté entre 0 y 1. 

[2:21] Aquí C denota cualquier región en este espacio. Que puede tener cualquier forma.

Como estamos con variables contínuas, la suma es infinitesimal y por tanto es una integral.

[2:38] Tenemos dos distribuciones marginales, una para la longitud $P(l)$ y 

[2:44] otra para la anchura $P(w)$. 

[2:50] Estas a su vez son distribuciones contínuas de una sóla variable, y las obtenemos SUMANDO todos los posibles valores sobre la variable contraria. Que en este caso, como es una suma de infinitos valores continuos, pues es una integral.

[3:08] En la distribución marginal de la anchura, para obtener la probabilidad de cualquier valor de $w$, tenemos que integrar sobre todos los valores de la longitud $l$, y por tanto los límites de integración son 
entre 0 y 5.

[3:25] Y de manera análoga para la distribución marginal de la longitud $l$, con los límietes de integración en el rango válido de los valores de $w$.

[3:38] Fijémonos ahora en las distribuciones condicionales.

[3:42] Tenemos tantas condicionales como posibles valores de cada variable ... es decir INFINITAS, y lo expresamos ASUMIENDO que fijamos un valor para la variable que condiciona.

[4:02] Si nos centramos en $w$, observa cómo cambia la distribución condicional de l dado w, según fijamos un valor distinto para w.

[4:20] Es decir, para cada posible valor de $w$ hay una distribución de probabilidad para l distinta, que en realidad corresponde al corte NORMALIZADO sobre la conjunta. 

[4:39] NORMALIZADO porque en general, la integral de cualquier corte no suma 1, y por tanto nomralizamos usando la probabilidad del valor que fijamos
para w.

[4:51] Y lo mismo para la las distribciones condicionales de w dado l. Aunque en este caso la normalización es
usando el valor que fijamos para l.

[5:02] Recuerda que si por ejemplo queremos expresar la distribución condicional de l respecto a un valor concreto de w, lo haríamos de la siguiente manera

$$P(l|w=2.1)$$

[5:25] y si queremos expresar esa distribución condicional de manera general, sin establecer un valor concreto
para w, lo expresaríamos de la siguiente manera.

$$P(w|l)$$

[5:31] sin olvidar que si finalmente queremos obtener valores de probabilidad concretos, tendremos que establecer, antes o después, un valor para $l$.


en resúmen, recuerda que

[5:53] la distribución conjunta contiene toda la información
[6:02] - una distribución marginal es la conjunta agregada sobre una de las variables
[6:15] - y una distribución condicional es un corte de la conjunta, que hay que normalizar para que sea una distribución de probabilidad correcta.
[6:30] la relación entre ellas es esta.






