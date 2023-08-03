```{post} 2023-07-24
:author: "GuayaHack"
:tags: organización, infraestructura, back-office
:category: wiki
:language: Español
:excerpt: 1
```

# Infraestructura GuayaHack

GuayaHack por ser una communidad física, digital y distribuida alrededor del mundo requiere de diferentes herramientas para cumplir con su {doc}`/community/memorial`. Eso, sin tener en cuenta que su enfoque principal es la tecnología e innovación para el progreso social, lo cual requiere espacios, digitales y/o físicos, para experimentar.

Por éstos motivos hacemos uso de varias herramientas, digitales y físicas, que llamamos infraestructura, ésta abarca todo lo que GuayaHack utiliza para el cumplimiento de su propósito.


## Redes Sociales

GuayaHack busca conectar a amantes de la tecnología entre si y a éstos con la sociedad en general, por éste motivo estamos presentes en las redes sociales du jour:

%#todo:project-idea
%#todo:investigar linkify no identifica bare links terminados en .social, la lista de dominios no esta desactualizada en upstream https://github.com/tsutsu3/linkify-it-py/blob/main/linkify_it/tlds.py

::::{grid} 4 4 4 4
:class-container: landing-grid
:gutter: 1

:::{grid-item-card}
:text-align: center
:link: https://guayahack.co
<i class="fa-solid fa-globe" style="font-size:2em"></i>
guayahack.co
:::

:::{grid-item-card}
:text-align: center
:link: https://mastodon.social/@guayahack
<i class="fa-brands fa-mastodon" style="font-size:2em"></i>
mastodon.social
:::

:::{grid-item-card}
:text-align: center
:link: https://matrix.to/#/!AkltWBgMvNJHuBhogU:matrix.org?via=matrix.org
<i class="fa-solid fa-m" style="font-size:2em"></i>
matrix.org
:::

:::{grid-item-card}
:text-align: center
:link: https://twitter.com/guayahack
<i class="fa-brands fa-twitter" style="font-size:2em"></i>
twitter.com
:::

:::{grid-item-card}
:text-align: center
:link: https://www.flickr.com/photos/guayahack/
<i class="fa-brands fa-flickr" style="font-size:2em"></i>
twitter.com
:::


:::{grid-item-card}
:text-align: center
:link: https://instagram.com/guayahack
<i class="fa-brands fa-instagram" style="font-size:2em"></i>
twitter.com
:::


:::{grid-item-card}
:text-align: center
:link: https://gitlab.com/guayahack
<i class="fa-brands fa-gitlab" style="font-size:2em"></i>
gitlab.com
:::

:::{grid-item-card}
:text-align: center
:link: https://github.com/guayahack
<i class="fa-brands fa-github" style="font-size:2em"></i>
github.com
:::

:::{grid-item-card}
:text-align: center
:link: https://twitch.com/guayahack
<i class="fa-brands fa-twitch" style="font-size:2em"></i>
twitch.com
:::

:::{grid-item-card}
:text-align: center
:link: https://youtube.com/guayahack
<i class="fa-brands fa-youtube" style="font-size:2em"></i>
youtube.com
:::

:::{grid-item-card}
:text-align: center
:link: https://reddit.com/guayahack
<i class="fa-brands fa-reddit" style="font-size:2em"></i>
reddit.com
:::

:::{grid-item-card}
:text-align: center
:link: https://linkedin.com/company/guayahack
<i class="fa-brands fa-linkedin" style="font-size:2em"></i>
linkedin.com
:::

:::{grid-item-card}
:text-align: center
:link: https://tiktok.com/guayahack
<i class="fa-brands fa-tiktok" style="font-size:2em"></i>
tiktok.com
:::

:::{grid-item-card}
:text-align: center
:link: https://snapchat.com/guayahack
<i class="fa-brands fa-snapchat" style="font-size:2em"></i>
snapchat.com
:::

::::


GuayaHack también se esfuerza por conectar a los espacios cuya filosofía se alinea con la nuestra, buscando regar la voz en lugares como [hackerspaces.org](https://wiki.hackerspaces.org/GuayaHack) entre otros.



## Gestión de Código

Si bien GitLab es el hogar de GuayaHack, por su flexibilidad y permitirnos ser parte de su programa "GitLab para Proyectos Open Source", no es de más tener presencia en otras plataformas: [GitLab](https://gitlab.com/guayahack), [GitHub](https://github.com/guayahack) y [BitBucket](https://bitbucket.com/guayahack).

Por su extensión, detalles sobre la administración de nuestro grupo [GuayaHack en GitLab](https://gitlab.com/guayahack.com) se encuentran en un artículo separado titulado {doc}`infraestructura-gitlab`

## Gestión de Documentos

### Google Drive

En GuayaHack tenemos una carpeta raíz en Google Drive la cual usamos para compartir documentos algo voluminosos que no tienen cabida en un repositorio Git o en GitLab como pdfs de libros o presentaciones, imágenes o arte y demás.

### Carpeta Raíz

El acceso a la carpeta raíz será proporcionado "on a need to know basis" a quienes *realmente* lo requieran, como excepción y contradiciendo el principio de transparencia de GuayaHack, ya que puede contener información de caracter privado.

```{figure} infraestructura.md-data/google-drive.png
---
---
Carpeta Raíz GuayaHack en GoogleDrive
```

### Carpeta Pública

Todo moderador y tutor que lo desee podrá recibir acceso de edición a ésta carpeta a fin de poder compartir sus materiales con autonomía. 

Aunque en GuayaHack creemos en el libre flujo de la información, no apoyamos, impulsamos o promulgamos la pirateria y ésta carpeta no es el espacio para hospedar contenido que infrinca la propiedad intelectual de personas ni organizaciones.

Miembros que deseen compartir sus materiales con la comunidad pueden contactar a cualquier tutor o moderador para que éste coordine su adición.

```{figure} infraestructura.md-data/google-drive-public.png
---
---
Carpeta Pública GuayaHack en GoogleDrive
```

## Gestion de Miembros y Staff

### GitLab

Por el momento GitLab es la SoT (Source of Truth) en cuanto a los miembros de GuayaHack respecta. El grupo en GitLab de [Miembros](https://gitlab.com/groups/guayahack/members/-/group_members), [Moderadores](https://gitlab.com/groups/guayahack/moderators/-/group_members) y [Maintainers](https://gitlab.com/groups/guayahack/maintainers/-/group_members) debera ser mantenido al día conforme los miembros se unan y entren en estado inactivo o en caso de extremas fallas de conducta sean removidos. 

### Google Groups

En Google Groups tambien tenemos dos grupos en caso que a futuro sea necesario tener listas de correo separadas o grupos que nos permitan gestionar el acceso a servicios y recursos de Google.

Por ahora el grupo `guayahack-staff@googlegroups.com` se utiliza para dar acceso de edición al Staff del [Calendario](https://calendar.google.com/calendar/u/0?cid=Z3VheWFoYWNrQGdtYWlsLmNvbQ) y a la [Carpeta Raíz de GuayaHack](https://drive.google.com/drive/folders/1sGunDL5EZ6MArx6jsxXsr_NXLqwB6nmW?usp=drive_link)
