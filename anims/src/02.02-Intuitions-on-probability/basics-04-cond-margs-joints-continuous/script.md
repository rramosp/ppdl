las nociones de distribuciones conjuntas, marginales y condicionales son análogas cuando alguna de las variables (o todas) son continuas.

simplemente tenemos que tener en cuenta dos cosas:

- que tendremos que sustituir las sumatorias por integrales
- que tenemos que tener en cuenta el rango de soporte de cada variable para realizar las integrales en los intervalos correctos.

por ejemplo, supongamos que nos dan la siguiente distribución conjunta de dos variables contínuas. En el notebook a continuación vamos a ver en concreto de dónde puede salir la distribución y como manejarla.

Por ahora, enfoquémonos en cómo las nociones de las distirbuciones discretas las llevamos a distribuciones contínuas.

Tenemos dos variables que describen el largo $l$ y el ancho $w$ de ciertas especies de microorganismos.

El intervalo válido de valores para $l$ es entre 0 y 5mm, y para $w$ entre 0 y 1mm. Es decir, los bichitos que estamos considerando no excede en ningún caso esos valores. En realidad nunca tendríamos valores exactamente de cero, ni demasiado pequeños, pero considerémoslo así para no complicarnos.

Fíjate que tenemos una distribución de probabilidad conjunta

$$P(l,w)$$

Las condiciones que garantizan que tenemos una distribución de probabilidad son

- $\int_0^5 \int_0^1 P(l,w)\text{d}l \text{d}w = 1$
- $\int_C P(l,w)\text{d}C \in (0,1)$, siendo $C$ cualquier región 2D sobre $l$ y $w$.

tenemos, por tanto, dos distribuciones marginales, una para la longitud $P(l)$ y otra para la anchura $P(w)$. Estas a su vez son distribuciones contínuas, y las obtenemos SUMANDO todos los posibles valores sobre la variable contraria. Que este caso, como es una suma de infinitos valores continuos, pues es una integral

- $P(l) = \int_0^1 P(l,w)\text{d}w$
- $P(w) = \int_0^5 P(l,w)\text{d}l$

Y fìjate que tenemos tantas condicionales como posibles valores de cada variable ... es decir INFINITAS, y que lo expresamos ASUMIENDO que fijamos un valor para la variable que condiciona.

- $P(l|w) = \frac{P(l,w)}{P(w)}$ asumiendo que en algùn momento se fija un valor concreto para $w$

Fíjate como para cada posible valor de $w$ hay una distribución de probabilidad distinta, que en realidad corresponde al corte NORMALIZADO sobre la conjunta.

Y lo mismo para

- $P(w|l) = \frac{P(w,l)}{P(l)}$ asumiendo que en algùn momento se fija un valor concreto para $l$

en resúmen, recuerda que

- la distribución conjunta contiene toda la información
- una distribución marginal es la conjunta agregada sobre una de las variables
- y una distribución condicional es un corte de la conjunta






