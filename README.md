# RecipeBook - Gestión de recetas
RecipeBook es una aplicación para planificar semanalmente las comidas y gestionar tu lista de la compra en función de lo que quieras cocinar.

El objetivo final es desarrollar una aplicación que permita introducir o seleccionar los ingredientes disponibles en una nevera, crear tus propias recetas con estos ingredientes u obtener sugerencias de recetas para cualquier comida del día.

También permitirá buscar recetas en función de los ingredientes disponibles, identificando aquellos ingredientes que no estén disponibles y que sean necesarios comprar.

El proyecto se desarrolla como un proyecto personal orientado a poner en práctica conocimientos de desarrollo de software, diseño de bases de datos y arquitectura software.

# <u>V1 - MVP</u>
La primera versión se centra en la gestión básica de usuarios, neveras, ingredientes y recetas:

- Registro e inicio de sesión
- Edición del usuario
- Gestión de neveras
- Gestión de ingredientes
- Gestión de recetas
- Asociación de ingredientes a neveras (con cantidad y unidad)
- Asociación de ingredientes a recetas (con cantidad y unidad)

Las funcionalidades posteriores, incluida la integración con APIs externas, están en el [Roadmap](docs/roadmap.md).

## Entidades

### Entidades principales

- **User** — Usuario de la aplicación.
- **Fridge** — Nevera perteneciente a un usuario.
- **Ingredient** — Ingrediente del catálogo, reutilizable en neveras y recetas.
- **Recipe** — Receta creada por un usuario.

### Entidades auxiliares

- **Category** — Categoría opcional de una receta.
- **Area** — Área geográfica opcional de una receta.
- **Fridge_ingredient** — Ingrediente en una nevera, con cantidad y unidad.
- **Recipe_ingredient** — Ingrediente en una receta, con cantidad y unidad.

## Relaciones principales

```text
User 1:N Fridge
User 1:N Recipe
Category 1:N Recipe
Area     0:N Recipe        (una receta tiene 0..1 área)
Fridge 1:N Fridge_ingredient   N:1 Ingredient
Recipe 1:N Recipe_ingredient   N:1 Ingredient
```

# Stack tecnológico

- **Backend:** Python + FastAPI
- **Frontend:** React
- **Base de datos:** MySQL
- **ORM:** SQLAlchemy
- **Testing:** pytest
- **Contenedores:** Docker
- **API externa (Fase 6):** TheMealDB

# Documentación

- [Requisitos](docs/requirements.md)
- [Casos de uso](docs/use-cases.md)
- [Roadmap](docs/roadmap.md)
- [Arquitectura](docs/architecture.md)
- [Base de datos](docs/database/database.md)

# Enlaces de interés

API Recetas (integración posterior al MVP, Fase 6): https://www.themealdb.com/documentation#lookup