# RecipeBook - Gestión de recetas

RecipeBook es una aplicación para planificar semanalmente las comidas y gestionar la lista de la compra en función de las recetas que se quieran preparar.

El objetivo es desarrollar una aplicación que permita gestionar los ingredientes disponibles en una o varias neveras, crear recetas y facilitar la planificación de comidas y la elaboración de la lista de la compra.

El proyecto se desarrolla como un proyecto personal orientado a poner en práctica conocimientos de desarrollo de software, diseño de bases de datos y arquitectura de software.

## V1 - MVP

La primera versión se centra en la gestión básica de usuarios, neveras, ingredientes y recetas:

- Registro e inicio de sesión
- Edición del usuario
- Gestión de neveras
- Gestión de ingredientes
- Gestión de recetas
- Asociación de ingredientes a neveras, con cantidad y unidad
- Asociación de ingredientes a recetas, con cantidad y unidad

Las funcionalidades posteriores, incluida la integración con APIs externas, se desarrollarán progresivamente según el [Roadmap](docs/roadmap.md).

## Stack tecnológico

- **Backend:** Python + FastAPI
- **Frontend:** React
- **Base de datos:** MySQL
- **ORM:** SQLAlchemy
- **Testing:** pytest
- **Contenedores:** Docker
- **API externa:** TheMealDB

## Documentación

- [Requisitos](docs/requirements.md)
- [Casos de uso](docs/use-cases.md)
- [Roadmap](docs/roadmap.md)
- [Arquitectura](docs/architecture.md)
- [Base de datos](docs/database/database.md)

## Enlaces de interés

- [TheMealDB](https://www.themealdb.com/documentation#lookup)