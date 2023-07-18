
```{post} 2023-07-18
:author: "@danteboe"
:tags: nota, tarea
:category: miembros
:language: Español
:location: Colombia
:excerpt: 1
```

# Como Resolví {doc}`/tarea/on-boarding-git-gitlab`

Git es una poderosa herramienta que permite colaborar en equipo con otros desarrolladores. Personalmente, hasta este momento solo lo había usado para subir proyectos personales. PERO, para saber sacarle el jugo realmente, es importante aprender a usar sus funciones de colaboración.

Nota: para esta solución, se supone que tienes VS Code instalado. En lo personal, me gusta la facilidad con la que se pueden guardar los cambios que realizas con tu repositorio en GitLab.
`TODO`

## 1. Fork del repositorio principal.

`FORK` es el nombre que se le da al proceso mediante el cual tú creas una copia de determinado repositorio en tu propia cuenta. Esto significa que puedes hacer contribuciones a un repositorio incluso sin ser miembro del grupo de desarrollo. Los cambios que hagas no se guardarán en el repositorio original, a menos que hagas un `merge request.`

```{figure} danteboe.md-data/fork.png
---
name: fork-button
---
Usando el boton superior derecho, puedes hacer fork del repositorio.
```

## 2. Clonar tu fork usando Git.
Puedes seguir este tutorial para instalar [GitBash](https://www.educative.io/answers/how-to-install-git-bash-in-windows), que es la herramienta que personalmente uso.

Primero, debes dirigirte al directorio en donde quieres clonar tu proyecto. (Si no tienes experiencia navegando usando una consola, [este artículo](https://www.computerhope.com/issues/ch000795.htm) te puede resultar útil).

La ventana con los links aparece al dar click en el botón `Clone` que encuentras a la derecha.

```{figure} danteboe.md-data/clone.png
---
name: clone-button
---
Puedes copiar el link que aparece en Clone with HTTPS.
```
Ingresa lo siguiente en la consola de Git Bash.

```console
$ git clone <tu link>
```

En el directorio (carpeta) que clonaste tu proyecto, deberían aparecerte los archivos del proyecto. 

Primero, dirígete a `site\community\member\spaces\index.md`

En la parte inferior, deberías encontrar los espacios para poder ingresar tu usuario como parte de la comunidad. 

```{figure} danteboe.md-data/members.png
---
name: member-list
---
Usa alguno de los espacios disponibles para escribir tu nombre.
```
Después, puedes copiar la carpeta `template` dentro de la misma ruta. Asegúrate de cambiar el nombre a tu usuario para indicar que es tu espacio. Dentro de la carpeta, encontrarás un archivo llamado `manifest.md`. Modifica el documento a tu gusto, escribiendo una introducción de ti.

```{figure} danteboe.md-data/template.png
---
name: template
---
Acá podrás darte a conocer ante el mundo.
```
Cuando hayas acabado, es tiempo de hacer una `push request` con tu repositorio fork. Es decir, haremos que los cambios realizados aparezcan en GitLab.
Usando VS Code, es tan fácil como dirigirte al ícono de `branch`, y dando click a `stage all changes` en la parte superior izquierda.

```{figure} danteboe.md-data/stage_changes.png
---
name: stage-changes
---
Con esto, seleccionas qué cambios hechos quieres sincronizar con GitLab. En este caso son todos.
```
VS Code se encarga de hacer un resumen de los cambios hechos en el repositorio automáticamente. Ingresa el mensaje con el que quieras que aparezca tu contribución en la parte superior del documento. Finalmente, da clic arriba a la derecha en el checkmark.

```{figure} danteboe.md-data/first_commit.png
---
name: first-commit
---
```
En tu fork de gitlab, debería aparecerte una alerta así tras haber sincronizado tus cambios.
```{figure} danteboe.md-data/merge_request.png
---
name: merge-request
---
Dale click al boton.
```

```{figure} danteboe.md-data/merge_details.png
---
name: merge-details
---
En esta ventana, podrás dar más información sobre los cambios que quieres hacer sobre el proyecto principal, o la `master branch`. Cuando finalices, da click al final de la página en `Create merge request`
```
Ahora lo que queda es esperar a que aprueben tu solicitud. Si hay algún error, los tutores deberían de hacerte saberlo.