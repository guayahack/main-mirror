```{post} 2023-07-23
:author: "@jdsalaro"
:tags: cicd
:category: tareas
:language: Español
:location: Alemania
:excerpt: 1
```

# Entendiendo la Magia de CI/CD y Build Pipelines

Hola Chic@s, ya algun@s han logrado crear su `/member/espacio` en {doc}`/tarea/on-boarding-git-gitlab`, pero hay muchas cosas que ocurrieron mágicamente: por ejemplo la copia de los archivos de sus cambios (Merge Requests) al servidor web responsable por el servicio de https://guayahack.co.

Hasta ahora no nos ocupamos con preguntas como: 

- ¿quién le hace pruebas a mis cambios?
- ¿cómo llegan mis cambios al servidor?
- ¿quien es responsable de copiar el código de la página al servidor?

Todas éstas preguntas son muy importantes y el archivo `.gitlab-ci.yml`[^MAINGITLABYML] tiene *todas* las respuestas.

#todo:explicar la pipeline se ejecuta cada vez que se ejecuta un cambio
#todo:explicar el proyecto guayahack/main tiene pipelines configuradas y donde esta el archivo

[^MAINGITLABYML]:https://gitlab.com/guayahack/main/-/blob/master/.gitlab-ci.yml

## Tarea

### 0. Lectura

Lee sobre el concepto de CI/CD y Pipelines.

¿Qué entendiste y porque crees que esos conceptos son parte fundamental del desarrollo de software moderno?

### 1. Encuentra la Pipeline de tu Merge Request 

Recuerda la tarea {doc}`/tarea/on-boarding-git-gitlab` y el hecho que tus cambios los enviaste como Merge Request. Esa MR tuvo que haber desencadenado una pipeline como se mencionó anteriormente. 

Encuentra la pipeline desencadenada por tu MR y analiza el output del job `pages` y responde las siguientes preguntas:

- ¿Que vés? PISTA: https://en.wikipedia.org/wiki/YAML

- ¿Que es?  PISTA: https://alexmarket.medium.com/introducci%C3%B3n-a-ci-cd-con-gitlab-23d4e9cc6482


### 2. Analiza el archivo `.gitlab-ci.yml` 

Ahora, en `/guayahack/main` encuentra la definición de las Pipelines, debe verse así:

```bash
image: python:3.9-slim                                                 #todo:explicar pista: https://www.redhat.com/es/topics/containers/what-is-docker  

before_script:                                                         #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#before_script
  - python --version                                                   #todo:explicar pista: https://docs.python.org/3/using/cmdline.html#generic-options
  - pip --version                                                      #todo:explicar pista: https://www.freecodecamp.org/espanol/news/como-usar-pip-install-en-python/
  - pip install pipenv                                                 #todo:explicar pista: https://pipenv-es.readthedocs.io/es/latest/
  - cp site/Pipfile .                                                  #todo:explicar pista: https://man7.org/linux/man-pages/man1/cp.1.html
  - cp site/Pipfile.lock .                                             #todo:explicar pista: https://pipenv-es.readthedocs.io/es/latest/basics.html#ejemplo-de-pipfile-pipfile-lock
  - ls                                                                 #todo:explicar pista: https://man7.org/linux/man-pages/man1/ls.1.html 
  - pipenv install                                                     #todo:explicar pista: https://pipenv-es.readthedocs.io/es/latest/install.html#instalando-paquetes-para-tu-proyecto
  - pipenv graph                                                       #todo:explicar pista: https://pipenv-es.readthedocs.io/es/latest/#otros-comandos
  - apt-get update                                                     #todo:explicar pista: https://aws.amazon.com/es/compare/the-difference-between-apt-and-apt-get/

pages:                                                                 #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#pages 
  stage: deploy                                                      
  script:                                                              #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#stage
    - rm -rf public                                                    #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#script
    - mkdir public                                                     #todo:explicar pista: https://man7.org/linux/man-pages/man1/mkdir.1.html
    - pipenv run sphinx-build -n -b dirhtml site/ site/_build/dirhtml  #todo:explicar pista: https://davidcasr.medium.com/c%C3%B3mo-documentar-un-proyecto-django-con-sphinx-80e4a090896e
    - cp -r site/_build/dirhtml/* public/                              #todo:explicar pista: https://man7.org/linux/man-pages/man1/cp.1.html
    - ls -alR public                                                   #todo:explicar pista: https://man7.org/linux/man-pages/man1/ls.1.html 
  artifacts:                                                           #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#artifacts
    paths:                                                             #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#paths
       - public                                                        #todo:explicar 
  only:                                                                #todo:explicar pista: https://docs.gitlab.com/ee/ci/yaml/#only
    - master                                                           #todo:explicar
```

Investiga y explica que labor cumple cada linea en el `.gitlab-ci.yml` mostrado anteriormente.

Documenta tus explicaciones y tus notas de acuerdo con REGLA0x05 [^REGLA05] en un blogpost y ponlo en `/community/member/user/reporte-entendiendo-cicd`

[^REGLA05]:https://guayahack.co/community/rules/#x05-00-00-00

### 3. Revisa y Comenta el MR correspondiente al Reporte de otro Miembro

En la tecnología es importante poder hacerse entender y entender a los demás, por eso deberás buscar la MR de otro miembro donde prepararon su reporte. Revísalo, verifica que es correcto y comprensible. Finalmente ofrece preguntas o comentarios aclaratorios en la misma MR.


## Notas al Pie

+++
