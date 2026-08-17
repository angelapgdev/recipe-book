# Requisitos

## <u>V1 - MVP</u>

## Requisitos funcionales

### *Gestión de usuario*
- **RF1. Registro**: un usuario podrá registrarse en la aplicación aportando un correo, contraseña y nombre.
- **RF2. Autenticación**: un usuario registrado podrá iniciar sesión con su correo y contraseña.
- **RF3. Edición de usuario**: un usuario registrado podrá editar su nombre.

A partir de este momento se hará referencia a un usuario registrado como usuario.

### *Gestión de neveras*
- **RF4. Creación de nevera**: un usuario podrá crear una nevera asignándole un nombre y opcionalmente ingredientes.
- **RF5. Edición de nevera**: un usuario podrá editar el nombre y los ingredientes de su nevera.
- **RF6. Eliminación de nevera**: un usuario podrá eliminar sus neveras.
- **RF7. Lectura de neveras**: un usuario podrá consultar una nevera y listar sus neveras.

### *Gestión de ingredientes*
- **RF8. Gestión de ingredientes de una nevera**: un usuario podrá añadir, editar y eliminar ingredientes de sus neveras, indicando la cantidad y unidad disponibles.
- **RF9. Gestión de ingredientes de una receta**: un usuario podrá añadir, editar y eliminar los ingredientes de sus recetas, indicando la cantidad y unidad necesarias.

### *Gestión de recetas*
- **RF10. Creación de receta**: un usuario podrá crear una receta asignándole un nombre, ingredientes con las cantidades necesarias y los pasos a seguir. Opcionalmente podrá añadir una imagen, tiempo de elaboración, dificultad, categoría y región geográfica.
- **RF11. Edición de receta**: un usuario podrá editar los atributos y los ingredientes de sus recetas.
- **RF12. Eliminación de receta**: un usuario podrá eliminar sus recetas.
- **RF13. Lectura de recetas**: un usuario podrá consultar y listar sus recetas.
- **RF14. Acceso a recursos propios**: un usuario solo podrá consultar y gestionar sus propias neveras y recetas.

## Requisitos no funcionales

### *Seguridad*
- **RNF1. Contraseñas**: las contraseñas no se almacenarán en texto plano.

### *Tiempo de respuesta*
- **RNF2. Tiempo de respuesta**: las operaciones que no dependan de servicios externos deberán responder en condiciones normales en menos de 500 ms.
- **RNF3. Búsquedas**: las búsquedas sobre recetas almacenadas deberán responder en condiciones normales en menos de 500 ms.
- **RNF4. Servicios externos**: las operaciones que dependan de una API externa deberán gestionar correctamente errores, tiempos de espera y respuestas no disponibles.

### *Mantenibilidad*
- **RNF5. Arquitectura por capas**: el proyecto estará organizado por capas, separando la presentación, la lógica de negocio y el acceso a datos.
- **RNF6. Separación de responsabilidades**: cada componente deberá tener una responsabilidad claramente definida y minimizar el acoplamiento entre componentes.


## Futuras versiones

- **RFX. Guardado de receta externa**: un usuario podrá guardar en su cuenta una receta obtenida mediante una API externa.
- **RFX. Búsqueda de recetas externas**: un usuario podrá buscar recetas por nombre mediante una API externa. Los resultados obtenidos no se almacenarán automáticamente en la base de datos.
- **RFX. Consulta de receta externa**: un usuario podrá consultar el detalle de una receta obtenida mediante una API externa.