```{post} 2023-08-13
:tags: organización, linux, infraestructura
:category: wiki
:language: Español
:excerpt: 1
```

# Ejecutando el repositorio main en ubuntu 22.04

Luego de completar el primer reto de guayahack, surge la duda de algunos por saber si ¿Es posible ejecutar el repositorio en nuestra máquina? sin la necesidad de esperar a que nuestros cambios sean aprobados, incorporados en `master`, se le haga "build" a página y éstos cambios se vean reflejados https://guayahack.co.

Éste tutorial busca resolver la pregunta anterior configurando una máquina en Linux con la distribución de Ubuntu en su versión 22.04. Se debe tener en cuenta que las descargas de las dependencias funcionen, para que nuestro repositorio `main` clonado sea ejecutable en la máquina y visto desde el navegador, dependerá de la velocidad de su internet y memoria RAM de la máquina.

Si no sabes cuál es el primer reto aquí en {doc}`/reto/on-boarding-git-gitlab` y la solución paso a paso aquí en {doc}`/community/member/danteboe/nota-on-boarding-git-gitlab`

## Características de la máquina

La máquina utilizada en este tutorial utiliza estas características:

```{figure} infraestructura-ejecutando-repositorio-main.md-data/pc-features.png
Máquina virtual creada en virtual box para este tutorial.
```

## Instalación de dependencias

Lo que se debe hacer es instalar la herramienta [pipenv](https://pipenv.pypa.io/en/latest/) que tiene como propósito ayudar con la creación y gestión de proyectos Python en un llamado entorno virtual sin la necesidad de instalar librerías y dependencias en nuestra máquina que después eliminaremos porque no le damos otro uso. Así, las dependencias de la página de GuayaHack quedarán solo asociadas con el proyecto y no serán instaladas a nivel global en el sistema operativo.

Para instalar la herramienta usamos el siguiente comando:

```bash
sudo apt install python3-pip -y
```

Al terminar la instalación siempre verificamos que nuestra librería se encuentre disponible para utilizar:

```bash
pip3 --version
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/pip-version.png
```

Para empezar con nuestra instalación de python versión 3.9 en nuestra distribución necesitamos hacer lo siguiente:

Actualizamos los paquetes de nuestra distribución:

```bash
sudo apt update
```
Instalamos el paquete **software-properties-common** para manejar diferentes librerias de terceros.

```bash
sudo apt install software-properties-common -y
```

Agregamos el repositorio **deadsnakes** para agregar nuestras versiones más recientes de python.

```bash
sudo add-apt-repository ppa::deadsnakes/ppa
```

Y aceptamos presionando la tecla enter:

```{figure} infraestructura-ejecutando-repositorio-main.md-data/consola-docs-python-modules.png
```

Con la configuración previamente realizada, procedemos a instalar python version 3.9:

```bash
sudo apt install python3.9 -y
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/install-python.png
```

Escribimos en nuestra terminal **python3** y apretamos la tecla **TAB**

```{figure} infraestructura-ejecutando-repositorio-main.md-data/tab-python-version.png
```

Instalamos nuestra libreria **pipenv**

```bash
pip3 install pipenv
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/pipenv-install.png
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/pipenv-install-warning.png
```

Al terminar de instalar  `pipenv` no va a funcionar desde nuestra terminal, ya que no esta agregada a nuestras [variables de entorno](https://es.wikipedia.org/wiki/Variable_de_entorno#UNIX_/_GNU/Linux). Lo primero que hacemos antes de agregar una variable de entorno es saber como esta para poder contrastarla luego de agregar una nueva.

```bash
echo $PATH
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/print-path.png
```

Agregamos nuestra nueva variable como se menciona al final de la instalación de `pipenv` donde se resalta la ruta y la agregamos:

```bash
export PATH="/home/david/.local/bin:$PATH"
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/add-environment-variable.png
```

Volvemos a ver nuestras variables de entorno con nuestra nueva variable agregada: 

```bash
echo $PATH
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/printing-path-again.png
```

Una vez agregada la variable de entorno, verificamos que funcione nuestra libreria pipenv:

```bash
pipenv --version
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/print-pipenv-version.png
```


## Ejecución del repositorio

Con nuestra libreria `pipenv` instalada, lista para utilizar y nuestro proyecto main descargado.

Nos dirigimos a la carpeta de `main` desde la terminal y colocamos el comando para iniciar nuestro entorno virtual y esperamos hasta que se genere:

```bash
pipenv shell
```


```{figure} infraestructura-ejecutando-repositorio-main.md-data/executing-pipenv-shell.png
```

Verificamos que nuestra versión de python sea la 3.9

```bash
python --version
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/python-version-main-environment.png
```

Instalamos el paquete  [distutils](https://docs.python.org/3/library/distutils.html) el cuál permite crear e instalar módulos adicionales a la instalación de python. El paquete se instalará con la versión puntual de python3.9 y que permitirá que a la hora de ejecutar nuestra aplicación no tenga problemas:

```bash
sudo apt-get install python3.9-distutils -y
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/install-python-distutils.png
```

Finalmente instalamos la herramienta [tox](https://tox.wiki/en/4.6.4/) que nos permite administrar ambientes virtuales para automatizar y ejecutar pruebas:

```bash
pipenv install tox
```

```{figure} infraestructura-ejecutando-repositorio-main.md-data/install-tox.png
```

Y ejecutamos el siguiente comando y esperamos unos minutos:

```bash
python -m tox -e live
```

El comando anterior permite ejecutar el archivo tox.init en el cuál tenemos las dependencias necesarias para que funcione el ambiente virtual sin problemas.

```{figure} infraestructura-ejecutando-repositorio-main.md-data/executing-tox.png
```

Cuando finalice se visualizara en la parte resaltada de blanco en enlace para abrirlo desde nuestro navegador de preferencia, lo copiamos y pegamos:

```{figure} infraestructura-ejecutando-repositorio-main.md-data/compiling-files.png
```

Y finalmente podremos navegar al proyecto desde nuestra máquina local 🎉:

```{figure} infraestructura-ejecutando-repositorio-main.md-data/guayahack-blog.png
```
