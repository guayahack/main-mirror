```{post} 2023-07-23
:author: "GuayaHack"
:tags: newbie, git
:category: wiki
:language: Español
:excerpt: 1
```

# Estrategias de Branching

En el mundo de Git y GitLab existen muchas estrategias para realizar cambios a una base de código.

En general, se puede decir que existen dos escenarios. Primero, cuando no se tiene acceso al projecto directamente se crea un fork, es decir una *personal* del proyecto. Luego se le hacen los cambios necesarios y le pide a los administradores del proyecto de origen combinar los cambios del fork con el mismo.

```{figure} note-git-branching-estrategias.md-data/gitlab-button-fork.png
Haciendo fork a un repositorio en GitLab
```


Segundo, cuando se tiene acceso al proyecto directamente, se puede trabajar con ramas y solicitar una vez estén listos los cambios a quien tenga acceso a `master` que combine los cambios de la rama nueva con los cambios (tambien llamadas feature branches) con `master`.

```{figure} note-git-branching-estrategias.md-data/gitlab-project-branches.png
Ramas o branches en un repositorio Git en GitLab
```
