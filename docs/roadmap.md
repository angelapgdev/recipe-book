# Roadmap

> Cada desarrollo incluye la implementación de los tests correspondientes a la capa y responsabilidad involucrada:
> - Dominio → tests unitarios
> - Repositorios → tests de persistencia/repositorio
> - Casos de uso y servicios → tests de casos de uso
> - API → tests de endpoints e integración
> - Integraciones externas → tests de integración
>
> Una funcionalidad se considera completada cuando su implementación y los tests asociados están terminados.

## Fase 1 — Modelo de datos y dominio
- [x] Definir requisitos iniciales
- [x] Definir casos de uso
- [x] Diseñar modelo entidad-relación
- [x] Diseñar modelo lógico
- [x] Implementar entidades del dominio
- [x] Implementar relaciones entre entidades
- [ ] Implementar tests unitarios del dominio

## Fase 2 — Persistencia
- [ ] Definir interfaces de repositorio
- [ ] Implementar repositorio genérico
- [ ] Implementar repositorios específicos
- [ ] Configurar persistencia con SQLAlchemy
- [ ] Probar operaciones de persistencia

## Fase 3 — Casos de uso

### Usuarios
- [ ] Registrar usuario
- [ ] Iniciar sesión
- [ ] Consultar usuario
- [ ] Actualizar usuario

### Neveras
- [ ] Crear nevera
- [ ] Consultar nevera
- [ ] Listar neveras
- [ ] Actualizar nevera
- [ ] Eliminar nevera
- [ ] Gestionar ingredientes de una nevera

### Recetas
- [ ] Crear receta
- [ ] Consultar receta
- [ ] Listar recetas
- [ ] Actualizar receta
- [ ] Eliminar receta
- [ ] Gestionar ingredientes de una receta

> Los casos de uso y servicios incluyen sus correspondientes tests de casos de uso.

## Fase 4 — API
- [ ] Endpoints de usuarios
- [ ] Endpoints de neveras
- [ ] Endpoints de recetas
- [ ] Autenticación
- [ ] Validación
- [ ] Gestión de errores
- [ ] Tests de API e integración

## Fase 5 — Integración externa
- [ ] Integrar TheMealDB
- [ ] Buscar recetas externas
- [ ] Consultar recetas externas
- [ ] Guardar recetas externas
- [ ] Tests de integración con servicios externos

## Fase 6 — Funcionalidades de negocio
- [ ] Comparar ingredientes disponibles con una receta
- [ ] Detectar ingredientes faltantes
- [ ] Generar lista de la compra
- [ ] Sugerir recetas según ingredientes disponibles
- [ ] Tests de los servicios y reglas de negocio

## Fase 7 — Evolución
- [ ] Planificación semanal
- [ ] Recetas favoritas
- [ ] Notificaciones
- [ ] Tests asociados a cada nueva funcionalidad