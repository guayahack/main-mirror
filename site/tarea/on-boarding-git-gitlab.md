```{post} 2023-07-18
:author: "@jdsalaro"
:tags: newbie, git, gitlab
:category: tareas
:language: Español
:location: Alemania
:excerpt: 1
```

# Presentándose y Entendiendo GGG (GuayaHack, Git, GitLab)

Hola! Ésta es la primera tarea con la que todo newbie deberá comenzar. La programación no es diferente a muchas otras áreas en las cuales hay herramientas básicas cuyo uso es imprescindible. El carpintero usa sus martillos y el esculptor sus cinceles, el programador moderno, en cambio su entorno de desarrollo y herramientas para gestión de código y proyectos. 

Ya que GuayaHack es un espacio sin ánimo de lucro, creada y mantenida por voluntarios, necesitamos herramientas y procesos que nos ayuden a funcionar de manera eficiente, mientras que al mismo tiempo compartimos y ayudamos a todos los miembros a adquirir nuevas habilidades y compartir sus conocimientos.

En GuayaHack usamos muchas herramientas, como pueden ver en {doc}`/wiki/infraestructura`, pero las dos herramientas más importantes para todo novato son Git y GitLab.

## Introducción

### Nuestras Reglas

Aunque somos un proyecto joven hemos crecido considerablemente, ésto es una ventaja pero tambien requiere que pongamos atención a la cultura que queremos propiciar. Para ésto tenemos nuestro {doc}`/community/memorial` y nuestras {doc}`/community/rules`.  

Por favor échales un vistazo. Además, ya que GuayaHack es un espacio de todos, puedes hacernos saber a los moderadores si encontraste errores, inconsitencias o deseas cambiar algo a fin de mejorarlas.

### Gestión de código con Git 

Git es una herramienta de código abierto gratuita que los programadores utilizamos para organizar nuestro código, sobretodo cuanto estamos en proyectos con más personas. Así como todo bebé aprende a no interrumpir para poder comunicarse efectivamente, el programador neofito usualmente debería aprender a usar git para poder contribuir cambios y nuevas funciones  de forma ordenada a codigos fuente y proyectos que no le pertenecen. 

No permitas que la impaciencia te gane, pero tu uso de Git y GitLab nos permite a los voluntarios ayudarte de forma efectiva y eficiente al igual que mantener los cientos de documentos y programas pequeños y grandes creados por la comunidad sin caer en la locura :)

El flujo de trabajo con Git es universal y es como sigue:

```{figure} on-boarding-git-gitlab.md-data/git-basic-workflow.png
Flujo de trabajo básico con Git
```

En la imagen anterior puedes ver tanto los pasos como los comandos asociados con el proceso de gestionar código fuente.

#### Instalación

Git es una herramienta muy poderosa, por eso se han escrito libros y grabado videos incontables sobre su instalación y uso. Nosotros no necesitamos saber todo sobre Git, por ahora es suficiente instalarlo y poder utilizar las funciones básicas mostradas en el diagrama anterior. Puedes aprender como instalar Git en tu sistema en [El Libro de Git: Instalación](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) 

### Gestión de Código con GitLab

Como en muchas profesiones, existen dos habilidades fundamentales que todo programador debe utilizar y mejorar a lo largo de su carrera: aprender a aprender y aprender a organizarse. 

Éste proceso nunca termina, pues jamás aprendemos todo lo que hay por aprender y nunca nos organizamos de forma que nunca hay que volver a organizar o gestionar nuestro código, proyectos y demás.

Por éste motivo, las personas que trabajan con tecnología son amantes de herramientas que les permitan organizarse mejor y trabajar de forma más eficiente. 

Nosotros en GuayaHack utilizamos https://gitlab.com, la plataforma de una empresa Estadounidense que, al igual que otras como GitHub o BitBucket, es utilizada por millones de programadores para gestionar su código y sus proyectos. 

Ya que GuayaHack hace parte de el programa de GitLab para Proyectos de código abierto[^GITLABOPENSOURCE], ellos nos han donado las licencias que utilizarán para trabajar.

[^GITLABOPENSOURCE]:https://about.gitlab.com/solutions/open-source/

```{figure} on-boarding-git-gitlab.md-data/gitlab-project.png
Proyecto de GuayaHack en GitLab
```

## Propósito

El propósito de ésta tarea es que te diviertas y aprendás a usar las herramientas básicas que utilizaremos para comunicarnos y organizarnos entre nosotros: Discord, Git, GitLab y el editor que elijas (VSCode, Sublime, VIM, NeoVim, EMACS, Nano y demás). En nuestra WIKI puedes encontrar dos artículos sobre el uso de VSCode ({doc}`/wiki/tutorial-intro-usar-vscode`) y el uso de VSCode con Git({doc}`/wiki/tutorial-intro-usar-git-vscode`) 

Carpintero a tu zapato, pero después de saber usar las herramientas :)

## Objetivo

Tú objetivo será `1` crear tu espacio en GuayaHack, crear tu `index.md` de presentación similar a {doc}`/community/member/jdsalaro/index` y `2` agregar tu nombre a la lista de miembros en {doc}`/community/index` enlazándolo con `1`. 

## Información adicional 

### Registrándote en GitLab


```{figure} on-boarding-git-gitlab.md-data/gitlab-registration.png
Registrándote en GitLab
```


## Pasos

### Solicitando acceso a `/guayahack/members`

```{figure} on-boarding-git-gitlab.md-data/gitlab-project.png
Solicitando acceso al grupo de GuayaHack en GitLab
```


### Verificando que tienes acceso a `/guayahack/members`

### Clonando main @ GuayaHack

```
git clone git@gitlab.com:guayahack/main.git
```

### Creando tu rama o branch

```
git checkout -b <REEMPLAZAR>
```


### Realizando cambios y haciendo push

```
# Agrega todos los archivos del directorio actual al stage 

git add . 

# Agrega la descripción del commit al stage

git commit -m "<REEMPLAZAR>" 

# Envía los datos al "origin" (la rama del repositorio REMOTO, aka Gitlab)

git push 
```

Verifica en el projecto de `/guayahack/main/` que puedes ver tu nueva rama creada.

```{figure} on-boarding-git-gitlab.md-data/gitlab-project-branches.png
Lista de ramas en un repositorio Git hospedado en GitLab
```

### Creando un Merge, también llamado Pull, Request

Ahora deberás crear una solicitud de incorporación de cambios, también llamada Merge Request, basada en esa rama que creaste.

```{figure} on-boarding-git-gitlab.md-data/gitlab-project-branches-new-mr.png
Creando una nueva Merge Request en GitLab
```

Recuerda, de ahora en adelante, que una Merge Request siempre está basada en la versión más actualizada de una rama o branch; puedes leer más sobre ésto en {doc}`/wiki/note-git-branching-estrategias`.


```{figure} on-boarding-git-gitlab.md-data/gitlab-branch-new-merge-request.png
Editando una nueva Merge Request
```


### Verificando Cambios

Ahora, verifica que todos tus cambios se ven como lo planeaste:

```{figure} on-boarding-git-gitlab.md-data/gitlab-mr-view.png
Vista de una Merge Request recién creada
```

Mira que el texto, las imágenes, todo está correcto.

```{figure} on-boarding-git-gitlab.md-data/gitlab-mr-changes.png
Cambios realizados en una Merge Request
```

## Aprobación e incorporación de cambios

Una vez tu hayas asignado a un moderador cómo reviewer o revisor de tu Merge Request, éste deberá aprobarla para que tu puedas hacerle "Merge" a tus cambios, es decir los puedas incorporar a `master` la rama principal del proyecto.


```{figure} on-boarding-git-gitlab.md-data/gitlab-mr-approval.png
Approvación de una Merge Request por parte de un Moderator
```



## Problemas Comunes

### Problema

En caso de que nos arroje un error de que no encuentra el origen, debemos agregar 

```
# Envía los datos al "origin"/<REEMPLAZAR> 

git push --set-upstream-to=origin/<REEMPLAZAR> 
```

## Pistas

En caso de necesitar un poquito de inspiración, puedes leer éste tutorial escrito por uno de nuestros miembros: {doc}`/community/member/danteboe/nota-on-boarding-git-gitlab`

