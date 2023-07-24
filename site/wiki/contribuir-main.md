```{post} 2023-06-30
:author: "GuayaHack"
:tags: newbie, organización, incompleto
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

### Contenido

El lenguaje de marcado que utilizamos es MyST; una extension de Markdown. Se pueden encontrar las siguientes convenciones:

```{figure} contribuir-main.md-data/convenciones-markdown.png
---
---
Convenciones Markdown
```


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

| categoría | descripción |
|-----------|-------------|
| escribir/write | para contribuir documentación que falta |
| fix/reparar | para resolver problemas en el código |
| ... | ... |
| ... | ... |

#### La WIKI

Los artículos de la WIKI no deberan tener autor ni ubicación, pues cambian y varían demasiado con el tiempo como para poder elegir a alguien en particular y tener una lista de contribuciones se vuelve tedioso. Para ver quienes han contribuido sobre el tiempo se puede utilizar GitLab y la commit history de git.

### Notas al Pie | Footnotes

Cuando usen notas al pie de página tipo `[^NOTA] ... [^NOTA]:LINK`, siempre debemos poner un header `# Notas al Pie` al final para que se vea bien.


## Troubleshooting

#todo:escribir
