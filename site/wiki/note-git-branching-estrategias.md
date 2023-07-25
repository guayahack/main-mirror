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

```{figure} note-git-commit-squashing.md-data/squash-commits-option-gitlab-mr.png)
Opción "Squash Commits" en una Merge Request de GitLab
```


Segundo, cuando se tiene acceso al proyecto directamente, se puede trabajar con ramas y solicitar una vez estén listos los cambios a quien tenga acceso a `master` que combine los cambios de la rama nueva con los cambios (tambien llamadas feature branches) con `master`.

```{figure} note-git-commit-squashing.md-data/squash-commits-option-gitlab-mr.png)
Opción "Squash Commits" en una Merge Request de GitLab
```


## ¿Qué es 'Commit Squashing'?

En Git, cada vez que hacemos un cambio en nuestro proyecto y guardamos ese cambio, lo llamamos un "commit". A veces, puedes encontrarte con una situación en la que has realizado muchos commits pequeños para una característica o corrección de errores en particular.

Aquí es donde entran los 'squash commits'. Básicamente, "comprimir" commits significa tomar una serie de commits y combinarlos en un solo commit. En lugar de tener un historial de cambios con muchos commits pequeños, tendrás un solo commit que representa todos esos cambios.

## ¿Por qué usar 'Commit Squashing'?

Aquí hay algunas razones por las que podrías querer usar 'squash commits':

1. **Mantiene tu historial limpio:** Un solo commit para una característica o corrección de errores hace que sea más fácil entender el historial de cambios en tu proyecto.

2. **Facilita la revisión de código:** Si tienes un único commit que representa todas las modificaciones realizadas, será más sencillo para otros revisar tu código.

3. **Ayuda a identificar y resolver problemas:** Si algo sale mal, puedes revertir fácilmente todo el conjunto de cambios simplemente deshaciendo ese único commit.

## ¿Cómo utilizar 'Commit Squashing' en GitLab?

Al hacer un 'merge request' en GitLab, existe una opción que dice "Squash commits". Al marcar esta opción antes de hacer clic en "Merge", GitLab automáticamente combinará todos tus commits en uno.

```{figure} note-git-commit-squashing.md-data/squash-commits-option-gitlab-mr.png)
Opción "Squash Commits" en una Merge Request de GitLab
```

Recuerda, el uso de 'squash commits' depende del flujo de trabajo de tu equipo y el tamaño y naturaleza de los cambios que estás haciendo. ¡Espero que esta información te sea útil y que ahora sientas más confianza al manejar tus proyectos en GitLab!
