# RecipeBook - Gestión de recetas
RecipeBook es una aplicación para planificar semanalmente las comidas y gestionar tu lista de la compra en función de lo que quieras cocinar.

El objetivo final es desarrollar una aplicación móvil que permita introducir o seleccionar los ingredientes disponibles en una nevera, crear tus propias recetas con estos ingredientes u obtener sugerencias de recetas para cualquier comida del día.

También permitirá buscar recetas en función de los ingredientes disponibles, identificando aquellos ingredientes que no estén disponibles y que sean necesarios comprar.

El proyecto se desarrolla como un proyecto personal orientado a poner en práctica conocimientos de desarrollo de software, diseño de bases de datos y arquitectura software.

# <u>V1 - MVP</u>
En una primera versión se desean abarcar esta serie de acciones.

- Registro e inicio de sesión.
- Gestión de neveras.
- Gestión de ingredientes.
- Gestión de recetas.

## Funcionalidades
1. Registro y autenticación.
2. Edición del nombre del usuario.
3. Población de tabla de ingredientes a través de una API externa.
4. Operaciones CRUD de neveras.
   1. Asociación de ingredientes a una nevera, ya sea introducciendo o seleccionando un ingrediente.
5. Operaciones CRUD de recetas.
   1. Asociación de ingredientes de una nevera a una receta.

Algunas de las funcionalidades de versiones posteriores están definidas y otras se irán definiendo a medida que avance el desarrollo (ver [Roadmap](docs/roadmap.md)).

## Entidades principales

- **Usuario** — Usuario de la aplicación.
- **Nevera** — Nevera perteneciente a un usuario.
- **Receta** — Receta creada por un usuario.
- **Ingrediente** — Ingrediente utilizado en una receta y almacenado en las neveras.

## Relaciones principales

```text
Usuario
   │
   ├── 1:N ── Nevera
   │             │
   │             └── N:M ── Ingrediente
   │
   └── 1:N ── Receta
                 │
                 └── N:M ── Ingrediente
```

# Stack tecnológico

- **Backend:** Python + FastAPI
- **Frontend:** React
- **Base de datos:** MySQL
- **ORM:** SQLAlchemy
- **Testing:** pytest
- **Contenedores:** Docker
- **API externa:** TheMealDB

# Documentación

- [Requisitos](docs/requirements.md)
- [Casos de uso](docs/use-cases.md)
- [Roadmap](docs/roadmap.md)
- [Arquitectura](docs/architecture.md)
- [Base de datos](docs/database/database.md)

# Enlaces de interés

API Recetas: https://www.themealdb.com/documentation#lookup