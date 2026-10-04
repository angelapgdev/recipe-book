# Arquitectura

## Objetivo

RecipeBook seguirá una arquitectura en capas basada en los principios de Clean Architecture, separando las responsabilidades de presentación, aplicación, dominio e infraestructura.

El objetivo es mantener el dominio independiente de los detalles técnicos, separar las responsabilidades y facilitar el mantenimiento, las pruebas y la evolución del sistema.

## Capas

```text
┌──────────────────────────┐
│       Presentation       │
│         FastAPI          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│       Application        │
│       Casos de uso       │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│          Domain          │
│  Entidades y contratos   │
└────────────▲─────────────┘
             │ implementa
┌──────────────────────────┐
│      Infrastructure      │
│ SQLAlchemy, MySQL, APIs  │
└──────────────────────────┘
```

Las dependencias de las capas deben dirigirse hacia las capas internas. El dominio no depende de detalles técnicos ni de frameworks externos.

La infraestructura implementa los contratos definidos por las capas internas.

## Domain

Contiene las entidades y reglas de negocio propias del dominio, así como los contratos que necesita el resto del sistema.

Incluye:

- Entidades de dominio.
- Enumeraciones.
- Reglas de negocio.
- Interfaces de repositorios.
- Excepciones de dominio.

El dominio no depende de FastAPI, SQLAlchemy, MySQL ni de servicios externos.

Las entidades de dominio deben representar conceptos y reglas del negocio sin estar acopladas al modelo de persistencia.

## Application

Contiene los casos de uso de la aplicación y coordina las operaciones necesarias para ejecutarlos.

Incluye:

- Casos de uso.
- Servicios de aplicación.
- Coordinación de operaciones.
- Gestión del flujo de ejecución de los casos de uso.

Por ejemplo:

- Registrar usuario.
- Iniciar sesión.
- Consultar usuario.
- Crear nevera.
- Gestionar ingredientes de una nevera.
- Crear receta.
- Gestionar ingredientes de una receta.

Los casos de uso utilizan las entidades del dominio y los contratos definidos por las capas internas, sin conocer los detalles de infraestructura.

La lógica específica de cada caso de uso se mantiene en esta capa, mientras que las reglas de negocio propias del dominio permanecen en Domain.

## Presentation

Contiene la interfaz HTTP de la aplicación mediante FastAPI.

Incluye:

- Routers y endpoints.
- Esquemas de entrada y salida.
- Validación de peticiones.
- Conversión de errores a respuestas HTTP.
- Gestión del contexto de autenticación de las peticiones.

La capa de presentación no contiene lógica de negocio ni accede directamente a la base de datos.

Su responsabilidad es adaptar las peticiones HTTP a los casos de uso y transformar sus resultados en respuestas HTTP.

## Infrastructure

Contiene las implementaciones concretas de los detalles técnicos utilizados por la aplicación.

Incluye:

- SQLAlchemy.
- MySQL.
- Modelos ORM.
- Mapeadores entre dominio y persistencia.
- Implementaciones concretas de repositorios.
- Hash de contraseñas.
- JWT.
- Integraciones con APIs externas.

Las implementaciones de infraestructura cumplen los contratos definidos por las capas internas.

La infraestructura puede depender de frameworks, librerías, bases de datos y servicios externos, ya que estos elementos son detalles técnicos del sistema.

## Estructura del proyecto

La organización prevista para el backend será:

```text
backend/
└── recipes/
    ├── domain/
    │   ├── models/
    │   └── repositories/
    │
    ├── application/
    │   └── use_cases/
    │
    ├── infrastructure/
    │   └── persistence/
    │       └── sqlalchemy/
    │           ├── models/
    │           ├── mappers/
    │           └── repositories/
    │
    └── presentation/
        └── api/
```

La estructura podrá evolucionar conforme aumente el tamaño de la aplicación, manteniendo la separación de responsabilidades definida en esta arquitectura.

## Casos de uso

Los casos de uso se encuentran en `application/use_cases/`.

Cada caso de uso representa una operación que el sistema permite realizar y coordina las entidades, reglas y repositorios necesarios para ejecutarla.

Por ejemplo:

```text
POST /users
     ↓
Presentation
     ↓
CreateUser
     ↓
UserRepository
     ↓
Infrastructure
     ↓
MySQL
```

La capa de presentación inicia la operación, el caso de uso coordina su ejecución y los repositorios proporcionan el acceso a los datos mediante sus contratos.

## Repository Pattern

Los contratos de repositorio se definen en el dominio y sus implementaciones concretas se encuentran en infraestructura.

```text
Application
     ↓
Repository Interface
     ↑
Concrete Repository
     ↓
SQLAlchemy
     ↓
MySQL
```

Los casos de uso trabajan con las interfaces de repositorio y no conocen SQLAlchemy ni MySQL.

Los repositorios se definirán principalmente para las entidades o agregados que necesiten operaciones de persistencia. Las entidades intermedias utilizadas para representar relaciones con atributos, como `FridgeIngredient` y `RecipeIngredient`, no requieren necesariamente un repositorio independiente.

## Inyección de dependencias

La infraestructura se conectará con los casos de uso mediante inyección de dependencias.

Los casos de uso recibirán las interfaces de repositorio que necesitan, mientras que la implementación concreta será proporcionada desde el exterior de las capas internas.

De esta forma, la aplicación puede trabajar con diferentes implementaciones de persistencia sin modificar la lógica de los casos de uso.

## Tests

Cada capa tendrá pruebas adaptadas a su responsabilidad:

- **Domain** → tests unitarios de entidades y reglas de negocio.
- **Application** → tests de casos de uso y servicios de aplicación.
- **Infrastructure** → tests de repositorios y persistencia.
- **Presentation** → tests de API e integración.
- **Integraciones externas** → tests de integración con servicios externos.

Una funcionalidad se considera completa cuando su implementación y las pruebas correspondientes están terminadas.

## Principios de dependencia

La arquitectura seguirá los siguientes principios:

- El dominio no depende de ninguna capa externa.
- Application depende de las abstracciones proporcionadas por Domain.
- Presentation utiliza los casos de uso de Application.
- Infrastructure implementa los contratos definidos por las capas internas.
- Presentation e Infrastructure no contienen reglas de negocio propias del dominio.
- El acceso a la base de datos se realiza exclusivamente mediante Infrastructure.
- Los casos de uso no conocen los detalles de SQLAlchemy, MySQL ni de otras tecnologías de persistencia.
- Las integraciones con servicios externos permanecen aisladas de las capas internas.

El objetivo es que los detalles técnicos puedan modificarse sin tener que modificar las reglas de negocio principales de RecipeBook.