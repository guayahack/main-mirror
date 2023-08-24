```{post} 2023-07-23
:tags: newbie, git
:category: wiki
:language: Español
:excerpt: 1
```

# Estrategias de Branching

En el mundo de Git y GitLab existen muchas estrategias para realizar cambios a una base de código. En general, se puede decir que existen dos escenarios. 

## Forks o bifurcaciones

Primero, cuando no se tiene acceso al projecto directamente se crea un fork, es decir una *personal* del proyecto. Luego se le hacen los cambios necesarios y le pide a los administradores del proyecto de origen combinar los cambios del fork con el mismo.

```{figure} note-git-branching-estrategias.md-data/gitlab-button-fork.png
Haciendo fork a un repositorio en GitLab
```

## Branches o ramas

Segundo, cuando se tiene acceso al proyecto directamente, se puede trabajar con ramas y solicitar una vez estén listos los cambios a quien tenga acceso a `master` que combine los cambios de la rama nueva con los cambios (tambien llamadas feature branches) con `master`.

```{figure} note-git-branching-estrategias.md-data/gitlab-project-branches.png
Ramas o branches en un repositorio Git en GitLab
```

## Merge Requests o solicitudes de incorporación

La incorporación de cambios utilizando Merge Requests, o Pull Requests como las llaman en GitHub, se puede dar de muchas formas, pero lo que sucede siempre es muy similar. En la siguiente figura se puede apreciar como toda Merge Request siempre esta asociada a una rama. Si se hacen cambios a una rama, la Merge Request asociada los contendrá.

```{figure} note-git-branching-estrategias.md-data/git-estrategias-branching.png
Merge Request basadas en `master` versus una basada en otra rama
```

Finalmente, cabe notar que no es bueno basar nuevas ramas y por ende otras Merge Request en ramas diferentes a `master`, pues éstas ramas que se usan como base pueden estár fuera de sincronía con `master` o estar `broken` en el sentido que contienen errores que no pueden ocurrir en `master` ya que ésta se monitorea más en detalle.
