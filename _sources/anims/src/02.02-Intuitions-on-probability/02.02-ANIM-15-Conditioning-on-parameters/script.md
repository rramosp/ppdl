
el flujo que hemos seguido en los ejemplos de los notebooks es que desde la distribución conjunta obtenemos las marginales y la condicionales que queramos.

y en el caso continuo hasta nos hemos empezado a encontrar con las primeras dificultades técnicas para manejas y calcular las integrales para normalizar las distribuciones condicionales.

pero no siempre vamos a tener este escenario.

a veces nos dan una distribución condicional, no la conjunta, quiza con una distribución marginal y a partir de ahì tenemos que trabajar.

Por ejemplo, supongamos que tenemos dos variables, w y l (como en el caso del dataset Abalon), pero en vez de darnos 
la distribución empírica con una tabla de datos, nos dicen que

w ~ Uniforme entre 0 y 1
l ~ Normal (mu = 2+w^2, sigma = 0.1 + w/2)

En realidad nos están diciendo que l depende de w y nos están dando la distribución de probabilidad de l para cada valor de w.

Es decir, nos están dando la probabilidad condicional P(l|w), porque para cada valor de w tendremos una distribución de probabilidad para l distinta.

Por ejemplo, esta es la distribución para P(l|w=0.4), y esta es la distribución para P(l|w=0.6)

De hecho, si queremos generar una muestra de la distribución conjunta podemos seguir el siguiente procedimiento

1- muestreamos w aleatoriamente entre 0. y 1 (una distribución uniforme)
2- muestreamos l de la distribución normal parametrizada por w

y vemos cómo se va revelando la distribución conjunta. Pero acordaros que nunca nos dieron la distribución conjunta.

De hecho la distribución conjunta es simplemente

P(l,w) = P(l|w)P(w)

que es la relación entre las tres distribuciones

P(l,w) = P(l|w)P(w) = P(w|l)P(l)


y lo puedes comprobar con este código

    from scipy.integrate import quad, dblquad

    p_w = lambda w: 1. 
    p_l_given_w = lambda w: stats.norm(loc=2+w**2, scale=.1+w/2).pdf
    p_lw = lambda l,w: p_l_given_w(w)(l)*p_w(w)

    dblquad(p_lw, 0, 1, lambda w: 0, lambda l: 5)

    >> 0.99999

$\int\int P(l|w)P(w)dldw = 1$ la integral da 1

y la marginal

$P(l) = \int P(l|w)dw$

y puedes comprobarlo con este código

    p_l = lambda l: quad(lambda w: p_l_given_w(w)(l), 0,1)[0]
    quad(p_l, 0,5)

    >> 0.99999

Fíjate que podemos considerar $w$ como un parámetro sobre el cual se construye la distribución de $l$.

En muchas ocasiones nos dan la distribución de UNA variable, como dependiente de unos parámetros.

Por ejemplo, nos dicen que $l$ sigue una distribución normal con $\mu$=2 y $\sigma$=0.5.

Esto es una distribución unidimensional, de una variable, que depende de dos parámetros para los que nos dan valores fíjos.

Una forma muy generalizada de expresar esto es la siguiente:

$P(l|\mu,\sigma) \sim \mathcal{N}(\mu, \sigma)$

Fíjate que la notación es la misma que la de probabilidad condicional. Como si tuviéramos una distribución conjunta de tres variables y condicionáramos en dos de ellas.

O si nos dan valores explícitos para $\mu$ y $\sigma$ sería

$P(l|\mu,\sigma) \sim \mathcal{N}(2, 0.5)$

De alguna manera estamos abusando de la notación, ya que $\mu$ y $\sigma$ NO SON variables aleatorias, sino parámetros.

Pero igual, yo puedo usar esta expresión para hacer muchas cosas. Por ejemplo, si yo tengo una observación de $l$ y expreso


$\text{argmax}_{\mu, \sigma}\;\; P(l|\mu, \sigma)$

yo estoy pidiendo los valores de $\mu$ y $\sigma$ que hacen que mi observación tenga la mayor probabilidad posible.

Veremos en los siguientes vídeos que esto nos va a ser de mucha utilidad cuando consideremos los conceptos de LIKELIHOOD.

Una cosa SUPER importante. En un momento dado, sí que podríamos considerar los parámetros como valores aleatorias y en este caso, estarían sujetos a sus propias distribuciones de probabilidad, y podríamos manejarlos dentro de cualquier aparato estadístico como cualquier otra variable.

Como por ejemplo dentro del teorema de bayes.

ESTO ES EL ASPECTO CENTRAL de la inferencia Bayesiana. Al considerar los parámetros de un modelo como distribuciones entramos en otr mundo. Cada parámetro ya no es un valor, sino una distribución completa, que es algo más complejo.

Esto lo veremos a partir del módulo 3.
