```{post} 2023-08-21
:author: "David Adarme"
:tags: newbie, uml, databases, erd, erm, cd
:category: wiki
:language: Español
:excerpt: 1
``` 

Bueno, me gustaría agradecer al parce {doc}`/community/member/jdsalaro/index` que ha creado esta [comunidad](https://guayahack.co) y por permitir compartir el conocimiento de él y otros usuarios más experimentados para apoyarnos a mejorar nuestras habilidades a nosotros, los amateurs/aficionados de la industria :)

Hace poco me salió la duda sobre la diferencia entre [Diagrama de Clases](#dc-cd-diagrama-de-clases-class-diagram) y [ Diagrama Entidad Relación](#der-erd-diagrama-entidad-relación-entity-relationship-diagram), la verdad es que son muy similares al menos en forma.

---

# 1. ¿Por qué la necesidad de los de diagramas en el desarrollo?

En primer término, los diagramas en el desarrollo son sumamente fundamentales al ejecutar proyectos, dado que nos sirven para simplificar y dividir procedimientos complejos en componentes mínimos debido a su formato gráfico. Una de las necesidades de los desarrolladores para realizar bosquejos y diagramas es poder encontrar problemas en una etapa inicial y no en producción, por ende éstos apoyan el mejoramiento de la calidad del software y el uso de buenas prácticas.

# 2 ¿Qué es UML?

Bueno, UML (_Unified Language Model-Lenguaje unificado de modelado_) es un lenguaje de modelado que sirve para visualizar, diseñar y documentar el software con sus respectivos procesos. Yo lo veo como una herramienta gráfica que ayuda a los desarrolladores a hacerle seguimiento a estructuras y el comportamiento de sistemas complejos.

Un ejemplo: 

´´´{figure} note-diferencias-diagrama-clases-entidad-relacion.md-data/uml.png
Ejemplo de UML
´´´

Éste tutorial es muy recomendable:

<iframe style="aspect-ratio: 16 / 9; width: 100%" src="https://www.youtube.com/embed/WnMQ8HlmeXc">
</iframe>

# 3 ¿Qué es un diagrama de clases(_CD_)?

Es una representación visual en la que se muestran las clases de objetos, así como sus atributos, métodos (Comportamiento) y las relaciones entre ellas. Es esencial ya que muestra la estructura y comportamientos posibles de un sistema al modelar las características que componen un **CD**.

Es útil para diseñar la arquitectura y las interacciones entre los componentes (Clases)

## 3.1 ¿Qué diagramas hay y cuál utilizar para cada caso en concreto?

### MER-ERM (Modelo Entidad Relación o Entity Relationship Model)

Es un modelo visual que muestra las entidades _(Persona, empresa, usuario, banco, etc.)_, atributos _(documento, tipo de documento, nombre, dirección, teléfono, correo, etc.)_, relación y proporción de relación _(1-1, 1-muchos, muchos-1, muchos-muchos, herencia, polimorfismo, etc.)_ entre diferentes elementos.

**Cuándo usarlo:** El MER se utiliza en la fase inicial del diseño de bases de datos para identificar y modelar las entidades, atributos y relaciones entre ellas.

´´´{figure} note-diferencias-diagrama-clases-entidad-relacion.md-data/uml-example.png
Ejemplo de Modelo Entidad Relación

´´´
### DER-ERD (Diagrama entidad relación-Entity relationship diagram)

El diagrama entidad relación es una representación gráfica del **Modelo de Entidad-Relación** que muestra  las entidades del sistema y sus relaciones internas. Su finalidad es mostrar de manera gráfica cómo las entidades se relacionan entre sí en un sistema o contexto determinado. La entidad puede considerarse como un sustantivo y la relación como un verbo.

Los DER son útiles para planificar y comunicar cómo se organizarán y relacionarán los datos en una base de datos antes de su implementación.

**Cuándo usarlo:** El DER se crea a partir del MER y se utiliza para representar gráficamente las entidades, atributos, relaciones y cardinalidades (ejemplo: 1:N) en una base de datos.

´´´{figure} note-diferencias-diagrama-clases-entidad-relacion.md-data/der.jpg
Ejemplo Diagrama Entidad Relación
´´´

### DC-CD (Diagrama de clases-Class diagram)

El diagrama de clase se utiliza para representar visualmente las clases, sus atributos, métodos y sus relaciones. Ayuda a entender la estructura del sistema, el comportamiento entre las clases _(entidades)_  y como se organizan los datos.

**Cuándo usarlo:** El Diagrama de Clases se utiliza en la programación orientada a objetos para representar las clases, sus atributos y relaciones en un sistema de software.

´´´{figure} note-diferencias-diagrama-clases-entidad-relacion.md-data/diagrama-de-clases.png
Ejemplo de Diagrama de Clases
´´´
---

## Notas al Pie

Tutorial de YouTube: [^UMLCOURSE].
[UMLCOURSE]: https://www.youtube.com/embed/WnMQ8HlmeXc

Modelo entidad-relación [^WIKIMER]
[WIKIMER]: https://es.wikipedia.org/wiki/Modelo_entidad-relaci%C3%B3n

¿Qué es un Diagrama de entidad relación? [^EDRAW]
[EDRAW]: https://www.edrawsoft.com/es/what-is-entity-relationship-diagram-erd.html

¿Qué es un diagrama entidad-relación? [^Lucidchart]
[Lucidchart]: https://www.lucidchart.com/pages/es/que-es-un-diagrama-entidad-relacion

Diagrama de clases - [^WIKIDC]
[WIKIDC]: https://es.wikipedia.org/wiki/Diagrama_de_clases

+++