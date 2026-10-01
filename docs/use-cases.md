# Casos de uso

## <u>V1 - MVP</u>

Todos los casos de uso de neveras y recetas se ejecutan sobre recursos propios del usuario (RF14).

### Actor: Usuario

#### Usuario
- **CU1**: Registrarse. (RF1)
- **CU2**: Iniciar sesión. (RF2)
- **CU3**: Consultar usuario. (RF3)
- **CU4**: Editar nombre de usuario. (RF3)

#### Neveras
- **CU5**: Crear nevera. (RF4)
- **CU6**: Consultar nevera. (RF7)
- **CU7**: Listar neveras. (RF7)
- **CU8**: Editar nevera. (RF5)
- **CU9**: Eliminar nevera. (RF6)

#### Ingredientes de una nevera
- **CU10**: Añadir o seleccionar un ingrediente para una nevera, indicando cantidad y unidad. Si el ingrediente no existe en el catálogo, se crea. (RF8)
- **CU11**: Editar la cantidad y la unidad de un ingrediente de una nevera. (RF8)
- **CU12**: Eliminar un ingrediente de una nevera. (RF8)

#### Recetas
- **CU13**: Crear receta. (RF10)
- **CU14**: Consultar receta. (RF13)
- **CU15**: Listar recetas. (RF13)
- **CU16**: Editar receta. (RF11)
- **CU17**: Eliminar receta. (RF12)

#### Ingredientes de una receta
- **CU18**: Añadir un ingrediente a una receta, indicando cantidad y unidad. El ingrediente se selecciona del catálogo o se crea; no tiene por qué estar en ninguna nevera. (RF9)
- **CU19**: Editar la cantidad y la unidad de un ingrediente de una receta. (RF9)
- **CU20**: Eliminar un ingrediente de una receta. No se puede eliminar el último. (RF9, RF10)