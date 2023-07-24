```{post} 2023-07-24
:author: "GuayaHack"
:tags: organización, infraestructura
:category: wiki
:language: Español, English, German
:excerpt: 1
```

# gitlab.com/guayahack

## Estructura de Permisos

La estructura de permisos de GuayaHack en GitLab no es muy compleja, pero si es lo suficientemente flexible para apoyar adecuadamente los procesos de la comunidad.

Todo miembro debe estar en *todos* los grupos que le corresponden. Un moderador, por ejemplo, debe estar en `/guayahack/members` y en `/guayahack/moderators`. Así, en caso de cambios en el grupo `/guayahack/moderators`, éste no perderá acceso por completo ya que lo mantiene a través de otros grupos. 

⚠️  En el caso de recursos, tanto grupos como proyectos, que son compartidos usando `share with` un miembro recibirá el nivel de permiso `max ( permiso en el grupo destino, permiso usado para share with) `. Es decir, daniel tendrá permisos de `developer` en `/guayahack/main`. 

```{figure} infraestructura-gitlab.md-data/gitlab-guayahack-permission-structure.png
---
---
Estructura de Permisos en GitLab/GuayaHack
```


