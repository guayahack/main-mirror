```{post} 2023-07-24
:tags: organización, infraestructura, gitlab, destacado
:category: wiki
:language: Español
:excerpt: 1
```

# Gestión de Nuestros Proyectos y Grupos en GitLab 

Nuestro código y proyectos para la organización y gestión de GuayaHack se encuentran GitLab bajo https://gitlab.com/guayhack. 


```{figure} infraestructura-gitlab.md-data/gitlab-group.png
Jerarquía principal de GuayaHack en GitLab
```

## Estructura de Permisos

La estructura de permisos de GuayaHack en GitLab no es muy compleja, pero si es lo suficientemente flexible para apoyar adecuadamente los procesos de la comunidad.

Todo miembro debe estar en *todos* los grupos que le corresponden. Un moderador, por ejemplo, debe estar en `/guayahack/members` y en `/guayahack/moderators`. Así, en caso de cambios en el grupo `/guayahack/moderators`, éste no perderá acceso por completo ya que lo mantiene a través de otros grupos. 

⚠️  En el caso de recursos, tanto grupos como proyectos, que son compartidos usando `share with` un miembro recibirá el nivel de permiso `max ( permiso en el grupo destino, permiso usado para share with) `. Es decir, daniel tendrá permisos de `developer` en `/guayahack/main`. 

```{figure} infraestructura-gitlab.md-data/gitlab-guayahack-permission-structure.png
Estructura de Permisos en GitLab/GuayaHack
```

### Gestión de Merge Requests

Ya que casi todo en GuayaHack occurre através de código y Merge Requests, es importante configurar los proyectos de forma que se nos haga más fácil la gestión de tantos cambios.

### CODEOWNERS [^GITLABDOCSCODEOWNERS]
[^GITLABDOCSCODEOWNERS]:https://docs.gitlab.com/ee/user/project/codeowners/index.html

Normalmente en GitLab todos los miembros de un proyecto a partir de `developer` pueden aprobar una Merge Request. Ésto no es ideal en nuestro caso ya que muchos {doc}`/wiki/organizacion-nivel-novato` tienen acceso a los proyectos pero no dominan aún bien las herramientas para saber cuando aprobar o no. De igual manera, algunos {doc}`/wiki/organizacion-rol-moderador` son moderadores por su compromiso con la comunidad, pero no dominan todavía los detalles de git y GitLab como para poder revisar y aprobar Merge Requests.

Por tanto es importante restringir aún más quien puede aprobarlas: sólo personas con acceso al projecto que *tambien* son miembros en https://gitlab.com/groups/guayahack/moderators/-/group_members

Aqui se puede ver, que con ésta configuración ya toda Merge Request requiere la aprobación de un Code Owner:

```{figure} infraestructura-gitlab.md-data/gitlab-project-require-code-owners-approval.png
Requisito de aprobación por parte de Code Owners https://gitlab.com/guayahack/main/-/blob/master/.gitlab/CODEOWNERS
```

Sin embargo, también es importante que un moderador no pueda aprobar su propia Merge Request:


```{figure} infraestructura-gitlab.md-data/gitlab-merge-request-required-approval-different-author.png
Requisito de aprobación por parte de alguien diferente al autor
```

En cuanto a mantener nuestros proyectos ordenados y su historia limpia, siempre le hacemos "squash" a los commits de ramas y sus Merge Requests. Una buena explicación de commit squashing está en la WIKI en {doc}`/wiki/note-git-commit-squashing`

```{figure} infraestructura-gitlab.md-data/gitlab-project-require-squash-commits.png
Requisito de "Squash Commits" en la configuración de `/guayahack/main`
```








