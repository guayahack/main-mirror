```{post} 2023-07-20
:author: "@mvykol"
:tags: diseño, css
:category: retos
:language: Español
:location: Colombia
:excerpt: 1
```

# Adaptando El /calendario a Dark-mode & Responsive

Mi metodologia para resolver un problema es muy sencilla y bastante
práctica en mi opinion, siempre me funciona.

No digo que esta sea la unica metodologia que deberian seguir, pero
es bueno tenerla en cuenta.

## 1. Crear una lista para estar organizados

Crear una simple `TODO-list` nunca es una mala idea, una vez tengas claro
Las cosas que hay que hacer, haz una pequeña lista:

* Averiguar como agregar CSS a un iFrame.
* Seleccionar paleta de colores para el calendario
* Probar como se ve en diferentes Browsers
* Que sea responsive (en otras palabras que se vea en pantallas pequeñas,
grandres, etc)

Puedes usar algo como notion, el mismo issue en GitLab o incluso un simple blog de notas, pero 
siempre ayuda tener una lista.

## 2. Leer Documentación, Stack Overflow, Google, ChatGPT

Ésta es la parte más importante, no importa si no sabes como hacer algo 
de memoria, buscar información es lo que más se hace cuando se esta desarrollando.

Lo mejor siempre es recurrir a la documentación, en este caso, la documentación de Google para ver como editar el calendario:
[support.google.com/calendar/](https://support.google.com/calendar/answer/41207?hl=en)

Si la documentación se te hace muy dificil de seguir, o sino está en castellano, siempre puedes recurir a chatGPT, pero *no te fies a ciegas*, porque no es perfecto, y si solo buscas con esta herramienta puede que pierdas mucho tiempo ya que chatGPT no está actualizado con la última información, y a veces alucina un poco.

Si sabes inglés, incluso un poco, como leer, puedes ir a Stack Overflow, 100% seguro alguien más tuvo el mismo problema que tu anteriormente [^STACKOVERFLOW].


[^STACKOVERFLOW]:https://stackoverflow.com/questions/4609742/adding-css-to-google-calendar-iframe



## 3. Implementation y resolución

En éste caso, averigué que el calendario de Google tiene propiedades que puedes editar en la URL, pero estas son limitandas. Si quieres editarlo totalmente a tu gusto, hay una API que se puede usar, pero el proceso cuesta de muchas lineas de código y simplemente no vale la pena, ya que terminarías haciendo tu propio calendario desde cero.

Encontré [éste post de Stack Overflow](https://stackoverflow.com/questions/42457368/google-maps-night-mode-embed-iframe) donde se refencia otro widget de Google usando iFrame, donde decía que si se invierte el filter, se podria hacer dark.


Funcionó, asi lo implementé en mi codigo, con algunos toques extras para que se vea mejor:

```
<iframe src="https://calendar.google.com/calendar/embed?
height=600&
wkst=1&
bgcolor=%2385ff54&
ctz=America%2FBogota&src=Z3VheWFoYWNrQGdtYWlsLmNvbQ&
color=%23039BE5" 

style="
border:solid 1px #777;
filter: invert(.9)
saturate(1.2) hue-rotate(145deg);
"  

width="800"

height="600"

frameborder="0"

scrolling="no">

</iframe>
```

## 4. Hacer Responsive

Despues solo faltaba hacerlo responsive, despues de buscar en Google por unos minutos, encontré [este post](https://thomas.vanhoutte.be/miniblog/make-google-calendar-iframe-responsive) de un blog que me ayudo.

### Markdown File

```html

<div class="responsiveCal">
<iframe src="https://calendar.google.com/calendar/embed?height=600&
wkst=1&
bgcolor=%2385ff54&
ctz=America%2FBogota&
src=Z3VheWFoYWNrQGdtYWlsLmNvbQ
&color=%23039BE5"

style="
border:solid 1px #777;
filter: invert(.9) saturate(1.2) hue-rotate(145deg);"

width="800"

height="600"

frameborder="0"

scrolling="no">

</iframe>
</div>
```

### CSS file

```

/*google calendar reponsiveness*/

@media screen and (max-width: 600px) {
    .responsiveCal {
        position: relative;
        padding-bottom: 130%;
        height: 0;
        overflow: hidden;
    }
    .responsiveCal iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
}

@media screen and (min-width: 700px) and ( max-width: 900px) {
    iFrame {
        width: 90vw;
    }
}

```

Funcionaba a la perfección, pero se veia mal en pantallas grandes[^ISSUERESPONSIVECAL], asi que agregué unas media queries[^MEDIAQUERY], una para pantallas pequeñas, y otra para pantallas medianas, [aqui](https://www.w3schools.com/css/css3_mediaqueries_ex.asp) puedes ver las media queries que usé.

[^MEDIAQUERY]:https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries

[^ISSUERESPONSIVECAL]:https://gitlab.com/guayahack/main/-/issues/14


Y voilà! Todo funciona como se esperaba!

## Resultados

`Browser (OperaGX)`


```{image} index.md-data/tuto.png
:alt: tuto
:width: 800px
:align: center
```

