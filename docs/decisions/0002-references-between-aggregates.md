# ADR-0002 — Referencias entre agregados y modelado de asociaciones

## Contexto

El dominio de RecipeBook contiene entidades relacionadas entre sí. En particular, una receta pertenece a una categoría y puede estar asociada a un área geográfica.

Aunque estas entidades están relacionadas, no necesariamente forman parte del mismo agregado. Las categorías y las áreas constituyen catálogos independientes que pueden ser compartidos por varias recetas.

También existen relaciones entre neveras e ingredientes, y entre recetas e ingredientes. Estas relaciones contienen información propia, como la cantidad y la unidad de medida de cada ingrediente.

Es necesario decidir cómo representar estas relaciones en el modelo de dominio, manteniendo los límites entre agregados, evitando dependencias innecesarias y permitiendo expresar las reglas de negocio.

La estructura de las tablas de la base de datos no determina por sí sola cómo deben representarse las relaciones en el dominio. Una tabla intermedia no implica necesariamente que deba existir una entidad independiente.

## Decisión

### 1. Referencias entre agregados independientes

Las referencias entre agregados independientes se representarán mediante sus identificadores (`UUID`), en lugar de mantener referencias directas a los objetos completos.

En consecuencia:

- `Recipe` tendrá los atributos `category_id` y `area_id`, siendo este último opcional.
- `Fridge` tendrá el atributo `user_id`, que identificará a su propietario.
- Las asociaciones con ingredientes utilizarán `ingredient_id` para referenciar al agregado `Ingredient`.

La existencia de los agregados referenciados se comprobará en los casos de uso correspondientes, mediante sus respectivos repositorios.

Los modelos de dominio no realizarán consultas directas a la base de datos para validar estas referencias.

### 2. Asociaciones con información propia

Cuando una relación contenga información relevante para el negocio, pero no necesite identidad propia, podrá representarse mediante un objeto de valor perteneciente a un agregado.

En RecipeBook se contemplan las siguientes asociaciones:

#### FridgeIngredient

`FridgeIngredient` representará la presencia de un ingrediente en una nevera y contendrá:

- `ingredient_id`: identificador del ingrediente.
- `quantity`: cantidad almacenada.
- `unit`: unidad de medida.

`Fridge` actuará como raíz del agregado y gestionará su colección de objetos `FridgeIngredient`.

Cada ingrediente podrá aparecer como máximo una vez en una misma nevera. Cuando cambie su cantidad o unidad, se actualizarán los datos de la asociación existente.

#### RecipeIngredient

`RecipeIngredient` representará la utilización de un ingrediente en una receta y contendrá:

- `ingredient_id`: identificador del ingrediente.
- `quantity`: cantidad necesaria.
- `unit`: unidad de medida.

`Recipe` actuará como raíz del agregado y gestionará su colección de objetos `RecipeIngredient`.

Inicialmente, cada ingrediente aparecerá como máximo una vez en una misma receta. Si cambian la cantidad o la unidad, se actualizarán los datos de la asociación existente.

### 3. Entidades y objetos de valor

Las entidades tienen una identidad propia que se mantiene aunque cambien sus atributos. Los objetos de valor, en cambio, se definen por sus atributos y no necesitan una identidad independiente.

Por tanto:

- `Fridge` y `Recipe` serán entidades y raíces de sus respectivos agregados.
- `Ingredient`, `Category` y `Area` serán entidades independientes.
- `FridgeIngredient` y `RecipeIngredient` se modelarán inicialmente como objetos de valor, sin identificador propio y sin heredar de `Entity`.

Los objetos de valor serán inmutables. Para modificar sus datos, se creará un nuevo objeto de valor que sustituya al anterior dentro de la colección del agregado.

Esta decisión podrá revisarse si aparecen requisitos que justifiquen una identidad independiente para alguna asociación.

### 4. Responsabilidades de los agregados

Las raíces de agregado serán responsables de mantener las invariantes de sus elementos internos.

Por ejemplo:

- `Fridge` gestionará las operaciones para añadir, actualizar y eliminar ingredientes de su colección.
- `Recipe` gestionará los ingredientes necesarios para su elaboración.
- Las asociaciones validarán sus propios atributos, como la cantidad y la unidad de medida, según las reglas de negocio definidas.

Las operaciones que requieran consultar o coordinar diferentes agregados se resolverán en la capa de aplicación.

## Alternativas consideradas

### Referenciar directamente las entidades relacionadas

Las entidades podrían mantener referencias a objetos completos, como `Category`, `Area`, `User` o `Ingredient`.

Esta opción facilita el acceso a sus atributos, pero introduce referencias directas entre agregados independientes y puede difuminar sus límites.

### Representar todas las relaciones exclusivamente mediante identificadores

Las entidades podrían almacenar listas de identificadores `UUID` para representar sus relaciones.

Esta alternativa simplifica las referencias, pero resulta insuficiente cuando una asociación necesita información propia, como cantidades o unidades de medida.

### Crear un agregado independiente por cada tabla intermedia

Las asociaciones podrían modelarse como agregados independientes, con sus propios identificadores, repositorios y operaciones.

Esta alternativa introduciría complejidad innecesaria mientras las asociaciones formen parte de las reglas de consistencia de `Fridge` y `Recipe` y no necesiten un ciclo de vida independiente.

### Representar las asociaciones como objetos de valor internos

Los agregados independientes se referencian mediante UUID, mientras que las asociaciones con información propia se representan mediante objetos de valor gestionados por sus raíces de agregado.

Esta es la alternativa adoptada porque mantiene los límites entre agregados y permite expresar las reglas de negocio sin introducir identidades innecesarias.

## Consecuencias

- Los agregados mantienen sus límites de consistencia.
- `Recipe` no necesita conocer la estructura interna de `Category` ni de `Area`.
- `Fridge` no necesita mantener una referencia directa al objeto `User`.
- Las asociaciones con ingredientes pueden representar cantidades y unidades de medida.
- `Fridge` y `Recipe` gestionan las reglas de negocio de sus respectivas colecciones.
- Las asociaciones no necesitan identificadores propios en el modelo de dominio.
- Los casos de uso coordinan las consultas necesarias para comprobar la existencia de referencias a otros agregados.
- La obtención conjunta de los datos relacionados se resolverá en la capa de aplicación o mediante las consultas de lectura apropiadas.
- La estructura del modelo de dominio no tiene por qué coincidir exactamente con la estructura de las tablas de la base de datos.
- La persistencia de los objetos de valor se realizará a través de los repositorios de los agregados correspondientes.

