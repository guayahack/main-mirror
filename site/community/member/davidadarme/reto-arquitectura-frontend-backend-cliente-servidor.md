 ```{post} 2023-09-03
:author: "@davidadarme"
:tags: newbie, frontend, backend, architecture
:category: retos
:language: Español
:excerpt: 1
``` 

# Introducción a la arquitectura frontend-backend o cliente-servidor

## Contexto e Introducción

El reto surgió debido a una exposición de proyecto que teníamos pendiente en el SENA y que debíamos presentar de acuerdo a los requisitos de entrega, los cuales incluían información sobre la arquitectura de software en la que estábamos trabajando. Por lo tanto, tenía dudas respecto a los conceptos de cómo está conformada la arquitectura de un aplicativo, y fue gracias a conversaciones con miembros de la comunidad sobre la arquitectura de aplicaciones que decidí aceptar un reto buscando entenderlo mejor. Éste artículo presenta mi solución al reto [Entender y explicar la arquitectura frontend-backend o cliente-servidor](https://gitlab.com/guayahack/main/-/issues/105), preparado por {doc}`/community/member/jdsalaro/index`.

### Agradecimientos

Gracias a {doc}`/community/member/jdsalaro/index` y @stween por ayudarme a obtener un concepto más solido sobre la arquitectura de software. Muy utíl en la exposición que realicé

## ¿Qué es hardware?

Son todos los componentes físicos de un medio informático como las partes físicas de una computadora o dispositivo electrónico, como la CPU, la memoria RAM, el disco duro, la placa madre, la pantalla, el teclado, el mouse, etc.

## ¿Qué es un sistema operativo?

El sistema operativo _(OS, por sus siglas en inglés, que significa Operating System)_ es un tipo de software intermediario que actúa como puente entre el hardware de una computadora y las aplicaciones que utilizan los usuarios. Un dato que me parece interesante es que los OS utilizan el lenguaje de bajo nivel[^WIKI-1], que es el tipo de lenguaje que interpreta el hardware, y el lenguaje de alto nivel, que es más cercano a como piensan y escriben código los humanos.
[^WIKI-1]: [Wikipedia - Lenguaje de bajo nivel](https://en.wikipedia.org/wiki/Low-level_programming_language)

## ¿Qué es una aplicación servidor (server application) y aplicación cliente (client application)?

**Aplicación Servidor (Application Server):** Es un software diseñado para ofrecer servicios y recursos a otras aplicaciones. Los servidores de aplicaciones[^WIKI] suelen manejar tareas como la gestión de transacciones, la seguridad, el manejo de bases de datos y la lógica empresarial (backend[^CODECADEMY]).
[^WIKI]: [Wikipedia - Servidor de aplicaciones](https://es.wikipedia.org/wiki/Servidor_de_aplicaciones)
[^CODEACADEMY]: [Codecademy - Arquitectura Backend](https://www.codecademy.com/article/back-end-architecture)

**Aplicación Cliente-Servidor (Client-Server):** es un modelo en el que las tareas se distribuyen entre los componentes cliente y servidor. El **cliente** como lo mencione anteriormente es el medio que solicita recursos al servidor mientras que el **servidor** es el sistema que proporciona esos recursos en respuesta a las solicitudes del cliente. Esta arquitectura es común en aplicaciones de red, como aplicaciones web y bases de datos [^WIKICS][^FLUFFY][^CLOUDFLARE].

[^WIKICS]: https://es.wikipedia.org/wiki/Cliente-servidor
[^CLOUDFLARE]: [Cloudflare](https://www.cloudflare.com/es-es/learning/serverless/glossary/client-side-vs-server-side/)
[^FLUFFY]: [Fluffy.es - Cliente servidor](https://fluffy.es/introduction-to-client-server)

> En una analogía, el chef es el servidor de aplicaciones y los platos de comida son los recursos o servicios que solicita a un cliente.

<iframe style="aspect-ratio: 16 / 9; width: 100%" src="https://www.youtube.com/watch?v=QSEDr2e1gSQ"></iframe>

## ¿Cómo se comunican el servidor y el cliente?

La comunicación entre el cliente (navegador web) y el servidor (donde reside el sitio web o la aplicación) se basa en el protocolo HTTP.

**HTTP _(Esp. Protocolo de transferencia de hipertexto/ Eng. Hypertext Transfer Protocol)_** permite que el cliente envíe solicitudes al servidor para obtener recursos, como datos, y el servidor responde con la información solicitada. Lee más acerca de HTTP[^HTTP]
[^HTTP]: https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto

**REST _(Esp. Transferencia de estado representacional/ Eng. Representational State Transfer)_**  utiliza HTTP para estructurar éstas solicitudes y respuestas, organizando los recursos en endpoints _(puntos finales)_ y utilizando los métodos HTTP _**(GET, POST, PUT, DELETE)**_ para realizar operaciones en esos recursos. Lee más acerca de REST[^REST]
[^REST]: https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional

## Otras tecnologías de la historia:

1. **CGI (Common Gateway Interface):** utilizada en los primeros días de la web, CGI permitía a los servidores web ejecutar programas externos para generar contenido dinámico en respuesta a las solicitudes del cliente. Aunque se ha vuelto menos común debido a su ineficiencia, sentó las bases para la interactividad en línea. Lee más acerca de CGI[^CGI]
[^CGI]: https://es.wikipedia.org/wiki/Interfaz_de_entrada_com%C3%BAn

2. **XML-RPC:** permitía la comunicación entre sistemas utilizando XML para codificar solicitudes y respuestas. Aunque menos eficiente que REST, fue una de las primeras tecnologías en permitir la integración entre aplicaciones y servicios web. Lee más acerca de XML-RPC[^XMLRPC]
[^XMLRPC]: https://es.wikipedia.org/wiki/XML-RPC

3. **SOAP (Simple Object Access Protocol):** Un protocolo de comunicación más complejo que XML-RPC, SOAP permitía la transmisión de mensajes estructurados entre aplicaciones a través de diversos protocolos, no solo HTTP. Lee más acerca de SOAP[^SOAP].
[^SOAP]: https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol

Cada una de estas tecnologías ha contribuido al desarrollo y la evolución de la comunicación cliente-servidor en la historia de la informática y la web.

## ¿Qué es lo que hoy en dia llamamos frontend?

El frontend se refiere a la parte visual y con la que interactúan los usuarios en una aplicación o sitio web, este se compone de diseño, la interfaz de usuario (GUI) y la presentación de la información.

## ¿Qué es lo que hoy en dia llamamos backend?

El backend es la parte "detrás de escena _(Behind The Scenes)_" de una aplicación o sitio web, donde se gestionan los datos, la lógica de funcionamiento y la comunicación con el servidor.

## Arquitectura de Comunicación Cliente-Servidor

```{figure} reto-arquitectura-frontend-backend-cliente-servidor.md-data/diagrama-cliente-servidor.png
Diagrama Cliente-Servidor
```

```{figure} reto-arquitectura-frontend-backend-cliente-servidor.md-data/diagrama-cliente-servidor-base-de-datos.png
Diagrama Cliente-Servidor y Base de datos
```

```{figure} reto-arquitectura-frontend-backend-cliente-servidor.md-data/arquitectura-tres-capas.png
Arquitectura de tres capas
```

## Conclusiones

En resumen, la arquitectura cliente-servidor es un tema fundamental en la informática, ya que facilita la comunicación entre componentes clave: el cliente, el servidor y el sistema operativo. Estos conceptos, en conjunto, sustentan el funcionamiento de aplicaciones y sistemas, conformando la base sobre la cual se construye la tecnología moderna.


## Notas al Pie
+++


