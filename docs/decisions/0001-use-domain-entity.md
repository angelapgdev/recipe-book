# ADR-0001 — Modelado de entidades del dominio

## Contexto

Las entidades del dominio necesitan una identidad propia que permita distinguir unas instancias de otras a lo largo de su ciclo de vida.

Inicialmente se planteó definir una abstracción `Identifiable` cuya responsabilidad sería establecer que una entidad dispone de un identificador mediante un método `get_id()`.

Sin embargo, al aplicar principios de Domain-Driven Design (DDD), se considera más adecuado representar explícitamente el concepto de **Entity** dentro del dominio.

Una entidad no se caracteriza únicamente por disponer de un identificador, sino porque su identidad permite distinguirla de otras instancias independientemente de sus atributos actuales.

Por ejemplo, dos recetas con el mismo nombre pueden representar entidades diferentes si tienen identificadores distintos.

## Decisión

Se utilizará una abstracción `Entity` dentro del dominio para representar el concepto de entidad e identidad.

Las entidades concretas del dominio podrán heredar de esta abstracción.

La identidad de las entidades se representará mediante `UUID`.

La abstracción `Entity` será independiente de cualquier mecanismo de persistencia o framework externo, como SQLAlchemy o MySQL.

Las entidades concretas del dominio serán objetos propios del dominio y no dependerán de modelos ORM.

## Alternativas consideradas

### Utilizar `Identifiable`

Se podría definir una abstracción `Identifiable` cuyo único objetivo fuera establecer que un objeto dispone de un identificador.

Se descarta porque expresa una característica técnica del objeto, pero no representa explícitamente el concepto de entidad dentro del dominio.

### No utilizar una abstracción común

Cada entidad podría definir directamente su identificador sin heredar de una abstracción común.

Esta opción reduciría el número de abstracciones, pero no permitiría expresar de forma explícita esta característica común del modelo de dominio.

## Consecuencias

- Las entidades del dominio tendrán una identidad explícita.
- El dominio permanecerá independiente de SQLAlchemy y de la base de datos.
- La identidad quedará diferenciada de los atributos de la entidad.
- Se establece una base para definir posteriormente las abstracciones de repositorio.
- No todos los objetos del dominio tendrán necesariamente que ser entidades.