```{post} 2023-07-23
:author: "GuayaHack"
:tags: newbie, git
:category: wiki
:language: Español
:excerpt: 1
```

# ¿Qué significa "squash commits" en Git y Gitlab?

**Simplifica tu Historial de Cambios con 'Squash Commits' en GitLab**

Hola a todos,

Hoy vamos a hablar sobre un tema importante en el mundo del control de versiones con Git y GitLab: el 'commit squashing' o "compresión de commits". Pero, ¿qué significa esto y por qué es tan útil? Vamos a profundizar.

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

```{figure} note-git-commit-squashing.md-data/squash-commits-option-gitlab-mr.png
Opción "Squash Commits" en una Merge Request de GitLab
```

Recuerda, el uso de 'squash commits' depende del flujo de trabajo de tu equipo y el tamaño y naturaleza de los cambios que estás haciendo. ¡Espero que esta información te sea útil y que ahora sientas más confianza al manejar tus proyectos en GitLab!
