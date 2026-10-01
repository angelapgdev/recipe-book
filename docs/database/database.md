# Modelo de datos

## Modelo entidad-relación

El siguiente diagrama representa el modelo conceptual de la base de datos de RecipeBook.

![Modelo entidad-relación](./er-diagram.png)

### Entidades

#### Usuario

Representa a un usuario registrado en la aplicación.

- id
- email
- password_hash
- nombre

#### Nevera

Representa una nevera perteneciente a un usuario.

- id
- nombre

#### Ingrediente

Representa un ingrediente reutilizable en recetas y neveras.

- id
- nombre

#### Receta

Representa una receta creada por un usuario.

- id
- nombre
- pasos
- imagen
- tiempo
- dificultad

#### Categoría

Representa una categoría a la que pertenece una receta.

- id
- nombre

#### Área

Representa el área geográfica o tradición culinaria asociada a una receta.

- id
- nombre

### Relaciones

- Un usuario puede tener varias neveras.
- Una nevera pertenece a un único usuario.
- Un usuario puede crear varias recetas.
- Una receta pertenece a un único usuario.
- Una categoría puede tener varias recetas.
- Una receta pertenece a una única categoría.
- Un área puede tener varias recetas.
- Una receta puede pertenecer a un área o a ninguna (0..1).
- Una nevera puede contener varios ingredientes.
- Un ingrediente puede estar presente en varias neveras.
- Una receta puede utilizar varios ingredientes.
- Un ingrediente puede utilizarse en varias recetas.
- Una nevera puede no contener ningún ingrediente.
- Una receta debe contener al menos un ingrediente.
- Un ingrediente del catálogo puede no estar asociado a ninguna nevera ni receta.

Las relaciones muchos a muchos entre `Nevera` e `Ingrediente`, y entre `Receta` e `Ingrediente`, se materializan mediante las entidades intermedias `Fridge_ingredient` y `Recipe_ingredient`.


## Modelo lógico

El siguiente diagrama representa el modelo lógico de la base de datos, incluyendo las claves primarias, claves foráneas, atributos y tablas intermedias.

![Modelo lógico](./logic-model.png)

### Fridge_ingredient

Entidad intermedia que representa los ingredientes almacenados en una nevera.

| Campo | Tipo | Clave |
|---|---|---|
| fridge_id | UUID | PK, FK → Fridge.id |
| ingredient_id | UUID | PK, FK → Ingredient.id |
| amount | decimal | |
| unit | IngredientUnit | |

La clave primaria está compuesta por `fridge_id` e `ingredient_id`, de forma que un mismo ingrediente no puede aparecer más de una vez en la misma nevera.

### Recipe_ingredient

Entidad intermedia que representa los ingredientes utilizados en una receta.

| Campo | Tipo | Clave |
|---|---|---|
| recipe_id | UUID | PK, FK → Recipe.id |
| ingredient_id | UUID | PK, FK → Ingredient.id |
| quantity | decimal | |
| unit | IngredientUnit | |

La clave primaria está compuesta por `recipe_id` e `ingredient_id`.

## Restricciones y decisiones de modelado

| Elemento | Regla |
|---|---|
| User.email | UNIQUE, NOT NULL |
| User.password_hash | NOT NULL; nunca se almacena la contraseña en claro (RNF1) |
| Ingredient.name | UNIQUE, NOT NULL (catálogo compartido entre usuarios) |
| Fridge.user_id, Recipe.user_id, Recipe.category_id | NOT NULL |
| Recipe.area_id | NULL permitido |
| Fridge_ingredient / Recipe_ingredient | `amount` > 0, `unit` NOT NULL |
| Recipe.steps | Lista ordenada de textos; se persiste como columna JSON |

Un ingrediente aparece como máximo una vez por nevera y una vez por receta (clave primaria compuesta).
Si los pasos pasan a tener atributos propios (imagen, temporizador), se normalizarán en una tabla `Recipe_step`.

## Enumeraciones

### RecipeDifficulty

Representa el nivel de dificultad de una receta.

- LOW
- MEDIUM
- HIGH

### IngredientUnit

Representa la unidad utilizada para expresar la cantidad de un ingrediente.

- UNIT
- GRAM
- KILOGRAM
- MILLILITER
- LITER
- TEASPOON
- TABLESPOON