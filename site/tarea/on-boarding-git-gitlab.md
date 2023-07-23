```{post} 2023-07-18
:author: "@jdsalaro"
:tags: newbie
:category: tareas
:language: Español
:location: Alemania
:excerpt: 1
```

# Presentándose y Entendiendo GGG (GuayaHack, Git, GitLab)

Ésta es la primera tarea con la que todo newbie deberá comenzar. 

## Objetivo

Tú objetivo será `1` crear tu espacio en GuayaHack y tu `index.md` de presentación similar a {doc}`/community/member/jdsalaro/index` y `2` agregar tu nombre a la lista de miembros en {doc}`/community/index` enlazándolo con `1`. 


## Guía 

### Clonando main @ GuayaHack

```
$ git clone git@gitlab.com:guayahack/main.git
```

### Creando tu Branch

```
$ git checkout -b {BRANCH_NAME}
```

### Realizando Cambios y Haciendo Push
```
$ git add . # Agrega todos los archivos del directorio actual al stage 
$ git commit -m "{COMMENT}" . # Agrega la descripción del commit al stage
$ git push # Envía los datos al "origin" (la rama del repositorio REMOTO, aka Gitlab)
```

### Abriendo un Merge/Pull Request

Lorem Ipsum


### Verificando Cambios

Lorem Ipsum






## Materiales y Herramientas

Lorem Ipsum



## Problemas Comunes

### Problema
En caso de que nos arroje un error de que no encuentra el origen, debemos agregar 
```
$ git push --set-upstream-to=origin/{BRANCH} # Envía los datos al "origin"/{BRANCH} 
```

#### Solución

Lorem Ipsum


