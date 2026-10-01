# Arquitectura

## Objetivo
RecipeBook seguirá una arquitectura en capas basada en los principios de Clean Architecture, separando las responsabilidades de presentación, aplicación, dominio e infraestructura.

El objetivo es mantener el dominio independiente de los detalles técnicos, separar las responsabilidades y facilitar el mantenimiento, las pruebas y la evolución del sistema.

## Capas

```text
┌──────────────────────┐
│    Presentation      │
│       FastAPI        │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│     Application      │
│     Casos de uso     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       Domain         │
│ Entidades y contratos│
└──────────────────────┘
           ↑
           │ implementa
┌──────────────────────┐
│   Infrastructure     │
│ SQLAlchemy, MySQL,   │
│ seguridad, APIs      │
└──────────────────────┘
```

## Domain
Contiene las entidades y reglas de negocio propias del dominio, así como los contratos que necesita el resto del sistema.

- Entidades de dominio.
- Enumeraciones.
- Reglas de negocio.
- Interfaces de repositorios.
- Excepciones de dominio.
  
El dominio no depende de FastAPI, SQLAlchemy, MySQL ni de servicios externos.

## Application
Contiene los casos de uso de la aplicación y coordina las operaciones necesarias para ejecutarlos. Por ejemplo:

- Registrar usuario.
- Iniciar sesión.
- Crear nevera.
- Crear receta.
- Añadir ingredientes a una receta.

Los casos de uso utilizan las entidades del dominio y los contratos definidos por las capas internas, sin conocer los detalles de infraestructura.

## Presentation
Contiene la interfaz HTTP de la aplicación mediante FastAPI.

- Routers y endpoints.
- Esquemas de entrada y salida.
- Validación de peticiones.
- Conversión de errores a respuestas HTTP.
- Autenticación de las peticiones.

La capa de presentación no contiene lógica de negocio ni accede directamente a la base de datos.

## Infrastructure
Contiene las implementaciones concretas de los detalles técnicos.

- SQLAlchemy.
- MySQL.
- Modelos ORM.
- Implementaciones de repositorios.
- Hash de contraseñas.
- JWT.
- Integraciones con APIs externas.

Las implementaciones de infraestructura cumplen los contratos definidos por las capas internas.

## Casos de uso

Los casos de uso se encuentran en application/use_cases/. Cada caso de uso representa una operación que el sistema permite realizar y coordina las entidades y repositorios necesarios. Por ejemplo:

```
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

## Repository Pattern

Los contratos de repositorio se definen en el dominio y sus implementaciones concretas se encuentran en infraestructura.

```
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

## Tests

Cada capa tendrá pruebas adaptadas a su responsabilidad:

- Domain → tests unitarios.
- Application → tests de casos de uso.
- Infrastructure → tests de repositorios y persistencia.
- Presentation → tests de API.
- Integraciones externas → tests de integración.

Una funcionalidad se considera completa cuando su implementación y las pruebas correspondientes están terminadas.