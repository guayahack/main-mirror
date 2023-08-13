```{post} 2023-06-30
:author: "GuayaHack"
:tags: newbie, organización
:category: wiki
:language: Español
:excerpt: 1
```

# Como Contribuir a la main @ GuayaHack

## Convenciones

### Secciones 

#### Notas al Pie

En caso de utilizar notas al pie en MyST o Markdown como `[^MYNOTAALPIE]`[^MYNOTAALPIE] y `[^MYNOTAALPIE]:https://es.wikipedia.org/wiki/Hacklab`

[^MYNOTAALPIE]:https://es.wikipedia.org/wiki/Hacklab

Debes agregar una sección `## Notas al Pie` al final de tu artículo y un break MyST[^MYST] `+++` para que no te aparezca un error por `` :

[^MYST]:https://jupyterbook.org/en/stable/reference/cheatsheet.html

```markdown
## Notas al Pie

+++
```

### Archivos

Para evitar errores y facilitar la busqueda de errores considera:
 
- No utilizar `_` (guión bajo), ` `(espacios) o signos `+` (mas) en nombres de archivos y carpetas. En su lugar, se debe utilizar `-` (guión)

- Los path de ubicación de archivos y referencias funcionan con  `/` (slash) en lugar de `\` (backslash)

- Trata de nombrar tus archivos de la manera mas corta pero comprensible posible, evitando palabras que no agregan mucho valor como `de`, `por`, `como`. 

- Si tu pagina cae en una categoria clara, por ejemplo un tutorial, considera nombra su archivo, y por tanto URL, `tutorial-...`.

#### Imágenes

- Las imágenes son una parte central de todo documento y en GuayaHack documentamos a fin de propiciar el entendimiento, un artículo con imágenes y ejemplos siempre será que uno sin ellas.

- Las imágenes, al igual que los [archivos](https://guayahack.co/wiki/contribuir-main/#archivos) deberán siempre tener un nombre claro que describa su propósito y contenido.

- Antes de utilizar imágenes y capturas de pantalla, verifica que éstas tienen una buena resolución y no están transformadas o distorsionadas (ensanchadas, alargadas y demás).

- Recuerda siempre revisar toda imagen que uses y censurarla apropiadamente de forma que información sensible ███████ no sea visible. Usa siempre un color con 100% de opacidad para censurar ya que de lo contrario será trivial incrementar el contraste de la imagen para revelar el contenido de la sección censurada.

### Contenido

El lenguaje de marcado que utilizamos es MyST; una extension de Markdown. Se pueden encontrar las siguientes convenciones:

```{figure} contribuir-main.md-data/convenciones-markdown.png
Convenciones Markdown
```

### Enlaces y fuentes

- En cuanto sea posible se deberán utilizar fuentes abiertas en el estilo de Wikipedia, no solo porque en GuayaHack apoyamos todo proyecto que contribuya al desarrollo de Internet sino también quienes apoyan la filosofías [Open Source](https://es.wikipedia.org/wiki/Sistema_de_c%C3%B3digo_abierto) y [Código Abierto](https://es.wikipedia.org/wiki/Software_libre)

### TODOs

Siempre en minúscula y con éste preciso formato: `#todo:categoría descripción`

### Metadatos y Encabezado ABlog

#### Formato

El encabezado no puede tener lineas vacías y debe estar al inicio de tu página:

:::
```{post} 2023-06-30
:author: "GuayaHack"
:tags: newbie, organización, incompleto
:category: wiki
:language: Español
:excerpt: 1
```
:::

De igual manera, los `tags` y la `category` deberán ir siempre en minúscula.

#### Categorias

Las categorías que tenemos son:

| categoría      | descripción                             |
| -------------- | --------------------------------------- |
| escribir/write | para contribuir documentación que falta |
| fix/reparar    | para resolver problemas en el código    |
| ...            | ...                                     |
| ...            | ...                                     |

#### La WIKI

Los artículos de la WIKI no deberan tener autor ni ubicación, pues cambian y varían demasiado con el tiempo como para poder elegir a alguien en particular y tener una lista de contribuciones se vuelve tedioso. Para ver quienes han contribuido sobre el tiempo se puede utilizar GitLab y la commit history de git.

### Notas al Pie | Footnotes

Cuando usen notas al pie de página tipo `[^NOTA] ... [^NOTA]:LINK`, siempre debemos poner un header `# Notas al Pie` al final para que se vea bien.


## Troubleshooting
Cuando se enfrenta a un problema, es indispensable reconocer las formas en las que se podría brindar solución. Por eso, aquí detallamos algunos elementos que se deben considerar:
1. <span style="color: green;">**Investigar**</span> la documentación de la tecnología a usar. 
2. <span style="color: green;">**Leer**</span> en foros especializados sobre algunos problemas similares que otros usuarios han encontrado en el proceso de utilizar dichas herramientas. 
3. <span style="color: green;">**Preguntar**</span> en los canales de texto de la comunidad oficial de Discord. Allí se podrá brindar apoyo sobre las dinámicas, herramientas u opciones. 
4. <span style="color: green;">**Compartir**</span> las soluciones, posibles y exitosas, a las que se llegue a partir de procesis de documentación. Recuerda que lo que te ayudó a ti, puede ayudar a otras personas. 
5. <span style="color: green;">**Agradecer**</span> a todo aquel que pueda ayudarte en esta travesía del conocimiento. 

`#todo:escribir`

## Revisando Merge Requests (MRs) 

Las solicitudes de incorporación de cambios, del inglés _Merge Requests_, son parte de todo proceso moderno de creación y gestión de software. Si bien la revisión de código es un arte y no una ciencia y por tanto no existen reglas universales, en GuayaHack tenemos un
par de pautas generales que todo Revisor de Código (Code Reviewer) deberá tener en cuenta:

- Sea respetuoso con sus comentarios y solicitudes, recuerde revisar con el próposito del cambio en mente, no con base en su opinion y preferencias.

- No existe Merge Request perfecta, a menos que sea realmente diminuta y en código irrelevante, por tanto siempre habrá comentarios que hacer. Esfúersece por encontrar el primer comentario y seguro encontrará el segundo, el tercero y el cuarto.

- El objetivo de una Code Review (Revisión de Código) no es que el revisor sea "cositero" y "corchador" sino que con sus comentarios contribuya a la mejora continua de los cambios y el estado de la base de código.

- No debe tener miedo de herir egos al sugerir cambios mientras sea respetuoso y no traiga el suyo y opiniones _infundadas_ al proceso de revisión. Toda MR es una conversación, trátela de ésta manera.

#todo:escribir
