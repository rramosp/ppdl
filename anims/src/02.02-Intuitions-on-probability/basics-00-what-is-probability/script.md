# talking about probability

**[00:00]** De manera general una distribución de probabilidad parte de un conjunto de objetos o propiedades o eventos o lo que sea con lo que estamos trabajando y les asigna porcentajes  [**anim x -> p(x)**]

**[00:12]** Por ejemplo, la distribución de probabilidad de un dado no trucado le asigna 1/6 de probabilidad a que salga cualquiera de los números. [**anim tabla 1-6 con probs**]

**[00:21]** Un distribución de probabilidad de las edades de una población, le puede asignar la frecuencia con la que se observan personas con cada rango de edad. [**anim histograma población**]

**[00:30]** Un modelo que clasifica imágenes de pacientes tratando de detectar una cierta patología nos puede dar una estimación de probabilidad que un caso tenga o no dicha patología [**anim modelo emitiendo predicción**]

**[00:42]** Por coherencia, y solemos expresar la probabilidad como un número entre cero y uno (a veces también como un porcentaje entre 0 y 100) y hay dos propiedades que cualquier distirbución de probabilidad debe de cumplir [**anim formulas**]

**[00:50]**
- 0 < p < 1
- sum 1

 
Pero no todas las distribuciones de probabilidad tienen el mismo significado y es muy importante saber qué estamos representando con una distribución de probabilidad 

por ejemplo

**[01:37]** podemos usar una distribución de probabilidad para describir todas las posibles sumas de dos dados lanzados al azar. hay 36 posibles combinaciones, sólo una de ellas suma 12, sólo otra una 2, pero hay 6 combinaciones que suman 7,  esta distribución describiría una realidad objetiva. [**anim combinaciones** ]

**[02:15]** también podemos usar una distribución de probabilidad para comunicar los resultados de un censo de la población, o de una encuesta de opinión. Fíjate que en estos casos la distribución representa una estimación de la realidad y, según el procedimiento que hayamos seguido, puede ser más o menos cercana a la misma. [**anim list of party A -> 50%, party B -> 40%, .. **]

**[03:20]** también podemos representar con una distribución de probabilidad nuestro grado de conocimiento o incertidumbre de algo, y actualizarla según aprendo cosas. por ejemplo, puedo representar mi desconocimiento de si llueve o no asignando un 0.5 a cada caso, pero si miro la ventana y veo nubes, a lo mejor le asigno 0.7 al caso con lluvia. Fíjate que en este caso, la distribución de probabilidad representa algo subjetivo (mi conocimiento o incertidumbre). [**anim sun/rain**]

**[04:10]** y ¿que representa la distribución de probabilidad que un modelo predictivo le asigna a una imagen de un paciente acerca de si tiene o no una patología? ... es una estimación ... un cálculo, que puede estar más o menos errado según muchas condiciones distintas ... si los datos eran suficientes, si el modelo es suficientemente complejo, si la patología es intrínsecamente difícil de separar, etc. [**anim model again**]

- y hay muchas otras circunstancias de uso de una distribución de probabilidad, a veces con significados muy diferentes. Así que siempre tenemos que tener cuidado de fijarnos bien en qué representa cualquier distribución de probabilidad que estemos manejando
 
**[05:05]** En el caso de machine learning, nos gustaría hacer varias cosas. Una de ellas es tratar adecuadamente la incertidumbre que rodea cualquier proceso con los datos.  [**anim clear, show "machine learning"**]

**[05:20]** puede que los datos tengan una aleatoriedad natural de la que no nos podemos deshacer (p.ej. con sensores ruidosos, o poblacines heterogéneas, etc.) ... pero nos gustaría poder manejarla, en el sentido de que nuestros modelos respondan distinto si esa incertidumbre es mayor o menor. [**some anim**]

**[05:52]** puede que la incertidumbre sea introducida por nuestro modelo, por la forma en la que los parametros del mismo capturan mejor o peor las relaciones entre los datos. [**anim model predict squigly**]

Podemos manejar todas estas incertidumbres con distribuciones de probabilidad. Si lo piensas, cada vez que tengamos un número podríamos tener una distribución de probabilidad, que represente nuestra incertidumbre sobre lo que representa ese número:

**[06:33]** La edad de un paciente --> la distribución de edades de los pacientes que estamos tratando [**number 32 transforming in gaussian**]
Un pixel en la posición x,y de una imagen --> la distribución de posibles valores de ese pixel

e incluso:
**[07:15]** e incluso un peso de una conexión entre dos neuronas --> una distribución de posibles valores para esa conexión [**anim neural network with distribuion**]

**[07:43]** el reto: que una distribución de probabilidad es algo más complejo que un sólo número. Un número es un escalar, una sola cantidad, pero una distribución de probabilidad son muchos números con una asignación de probabilidad a cada uno de ellos. 

**[08:15]** por tanto, vamos a tener que generar toda la maquinaria necesaria para manipular, procesar, transformar, combinar, ... distribuciones de probabilidad. [**anim transforming prob distributions**]

**[09:00]** imagínate una red neuronal en la que cada peso es una distribución de probabilidad, en vez de un número ... cómo generas una predicción?, cómo entrenas la red? [**anim wheely**]

esto es lo que vamos a aprender en este curso.
