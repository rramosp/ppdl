como te puedes imaginar existe una relación muy concreta entre las probabilidades conjuntas, marginales y condicionadas, de modo que cuando si tenemos la información suficiente podemos obtener unas de otras.

recuerda que en el ejemplo de ciudades y partidos tenemos dos variables aleatorias (Xp partidos, Xc ciudades) y que ambas son discretas. Tenemos cuatro partidos distintos y tres ciudades distintas.

partimos de que tenemos la distribución de probabilidad conjunta.

fíjate que por tanto tenemos

- dos distribuciones marginales, una por cada variable aleatoria, P(Xp) y P(Xc)
- cuatro distribuciones condicionales para P(Xc), una para cada valor de Xp: P(Xc|Xp=p1), P(Xc|Xp=p2), P(Xc|Xp=p3), P(Xc|Xp=p4)
- tres distribuciones condicionales pra P(Xp), una para cada valor de Xc: P(Xp|Xc=c1), P(Xp|Xc=c2), P(Xp|Xc=c3)

Las distribuciones condicionales se representan en muchas ocasiones sin expresar explícitamente el valor concreto que condiciona. 

Por ejemplo, solemos decir "tenemos la distribución P(Xc|Xp)", sin decir respecto a qué partido en concreto. 

Es importante darse cuenta que esto se hace como parte de algún argumento o planteamiento de un problema o solución. Cuando hacemos esto, en realidad estamos ASUMIENDO que en algún momento, se determinará un valor concreto para el valor que condiciona (un partido concreto si es Xp como en P(Xc|Xp) ), y de esta manera lo que hacemos es válido para cualquier valor.

Por ejemplo, si expreso

$$max_{X_p}\;\; P(X_p|X_c)$$

estoy preguntando por el porcentaje de votos del partido que ganó ASUMIENDO que fijo una ciudad.

Fíjate ahora cómo, a partir de la distribución conjunta, construímos las distribuciones marginales

- $P(X_p) = \sum_i P(X_p,X_c=c_i)$ con $i \in \{1,2,3\}$
- $P(X_c) = \sum_i P(X_p=p_i,X_c)$ con $i \in \{1,2,3,4\}$

y las condicionales:

- $P(X_p|X_c=acity) = \frac{P(X_p, X_c=acity)}{\sum_i P(X_p, X_c=c_i)} = \frac{P(X_p, X_c=acity)}{P(X_c=acity)}$

fíjate que el denominador de esta última expresión es un valor de distribución marginal de $X_c$

Por ejemplo,

- $P(X_p|X_c=city2) = \frac{P(X_p, X_c=city2)}{\sum_i P(X_p, X_c=c_i)}$ = $\frac{P(X_p, X_c=city2)}{0.142 + 0.241 + 0.031 + 0.099}$ = $\frac{P(X_p, X_c=city2)}{0.513}$

  
Por tanto $P(X_p|X_c=city2)$ = 

- $\frac{0.142}{0.513}=0.277$ si $X_p=p1$
- $\frac{0.241}{0.513}=0.470$ si $X_p=p2$
- $\frac{0.031}{0.513}=0.060$ si $X_p=p2$
- $\frac{0.099}{0.513}=0.193$ si $X_p=p2$

En el sentido que acabamos de hablar, la relación

$P(X_p|X_c=acity) = \frac{P(X_p, X_c=acity)}{P(X_c=acity)}$

se suele expresar de forma generalizada y abreviada de la siguiente manera

$$P(X_p|X_c) = \frac{P(X_p, X_c)}{P(X_c)}$$

y es la expresión que nos da la relación concreta que existe entre las distirbuciones conjuntas, marginales y condicionales.

que podemos escribir también de la siguiente manera

$$P(X_p|X_c)P(X_c) = P(X_p, X_c)$$

y también para la distribución condicional de $X_c$

$$P(X_c|X_p)P(X_p) = P(X_p, X_c)$$

y de donde surge de manera natural el teorema de bayes, que más adelante vamos a inspeccionar en detalle.

$P(X_p|X_c)P(X_c) = P(X_c|X_p)P(X_p)$

$\Rightarrow P(X_p|X_c) = \frac{P(X_c|X_p)P(X_p)}{P(X_c)}$ 

$\Rightarrow P(X_c|X_p) = \frac{P(X_p|X_c)P(X_c)}{P(X_p
)}$ 

Finalmente, ten en cuenta que esto lo podemos extender a distribuciones conjuntas de cualquier número de variables

$P(x,y,z,w)$

y podemos plantearnos por ejemplo marginalizar sobre cualquier número de ellas, simplemente tenemos que prestar atención a sumar bien sobre las variables adecuadas

- $P(x,y,z) = \sum_i P(x,y,z,w=w_i)$
- $P(x,y) = \sum_i \sum_j P(x,y,z=z_j,w=w_i)$
- $P(y,w) = \sum_l \sum_j P(x=x_l,y,z=z_j,w)$
- $P(x) = \sum_i \sum_j \sum_k P(x,y=y_k,z=z_j,w=w_i)$
- etc.

donde cada índice recorre todos los posibles valores de la variable correspondiente. Si $x$ tiene 5 valores, $l$ va de 1 a 5, si $y$ tiene 2 posibles valores, $k$ va de 1 a 2, etc.

Fíjate que, por ejemplo, $P(x,y,z)$ es una distribución conjunta de tres variables, obtenida MARGINALIZANDO sobre $w$ una distribución conjunta de cuatro variables, o que $P(x,y)$ es una distribución conjunta de 2 variables, obtenida marginalizando la distribución conjunta original sobre $z$ y $w$.

Y sucede lo mismo con las distribuciones condicionales. Podemos condicionar sobre el número de variables que queramos.

- $P(x,y,z|w=w_i) = \frac{P(x,y,z,w=w_i)}{\sum_i P(x,y,z,w=w_i)}$

o expresado de forma abreviada

- $P(x,y,z|w) = \frac{P(x,y,z,w)}{P(w)}$

asumiendo que se fija el valor de $w$

si seguimos condicionando

- $P(x,z|y,w) = \frac{P(x,y,z,w)}{P(y,w)}$, asumiendo que fijamos valores para $y$ y $w$
- $P(x|z,y,w) = \frac{P(x,y,z,w)}{P(z,y,w)}$, asumiendo que fijamos los valores de $y$, $w$ y $z$.

observa que, por ejemplo, $P(x,y,z|w)$ es a su vez una distribución conjunta de 3 variables y $ P(x,y|z,w)$ es una distirbución conjunta de 2 variables.
