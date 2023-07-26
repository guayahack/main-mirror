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

En GuayaHack usamos muchas herramientas, como pueden ver en {doc}`/wiki/infraestructura.md`, pero las dos herramientas más importantes para todo novato son Git y GitLab.

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

Ya que GuayaHack hace parte de el programa de GitLab para Proyectos de código abierto, ellos nos han donado las licencias que utilizarán para trabajar.

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

### Solicitando acceso a `/guayahack/members`

### Verificando que tienes acceso a `/guayahack/members`

### Clonando main @ GuayaHack

```
git clone git@gitlab.com:guayahack/main.git
```

### Creando tu rama o branch

```
git checkout -b {BRANCH_NAME}
```

### Realizando cambios y haciendo push

```
# Agrega todos los archivos del directorio actual al stage 
git add . 

# Agrega la descripción del commit al stage
git commit -m "{COMMENT}" . 

# Envía los datos al "origin" (la rama del repositorio REMOTO, aka Gitlab)
git push 
```

### Creando un Merge, tambien llamado Pull, Request

Lorem Ipsum

### Verificando Cambios

Lorem Ipsum

## Materiales y Herramientas

Lorem Ipsum



## Problemas Comunes

### Problema

En caso de que nos arroje un error de que no encuentra el origen, debemos agregar 

```
# Envía los datos al "origin"/{BRANCH} 

git push --set-upstream-to=origin/{BRANCH} 
```

#### Solución

Lorem Ipsum


