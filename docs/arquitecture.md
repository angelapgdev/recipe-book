# Arquitectura

## Objetivo

RecipeBook se desarrollará siguiendo una arquitectura en capas donde el diseño está guiado por el dominio (Domain-Driven Design - DDD).

El objetivo es mantener separadas las responsabilidades de presentación, aplicación, dominio e infraestructura, evitando que la lógica de negocio dependa directamente de la implementación consiguiendo así una arquitectura limpia que permita mantener el código, realizar pruebas de manera sencilla y que la evolución del sistema no este limitada.

## Principios arquitectónicos

El diseño se basa en los siguientes principios:

- Separación de responsabilidades.
- Encapsulación de la lógica de negocio.
- Dominio independiente de los detalles de infraestructura.
- Casos de uso explícitos.
- Bajo acoplamiento entre capas.
- Alta cohesión dentro de cada componente.
- Dependencias controladas entre capas.