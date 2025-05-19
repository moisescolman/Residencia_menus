# Residencia Menús – Base de Datos MongoDB

## Descripción del proyecto
Este proyecto implementa la **base de datos** para el sistema de gestión de menús en una residencia. Permite:
- Definir **residentes**, sus **alergias** y **tipos de dieta**.
- Crear y versionar **menús** (plantillas semanales) adaptados a distintos perfiles dietéticos.
- Gestionar el catálogo de **platos**, con sus ingredientes y alérgenos normalizados.
- Administrar **asignaciones** diarias de menús a residentes, incluyendo el servicio de **catering**.
- Registrar **incidencias** (p. ej. reacciones alérgicas, errores en la asignación).
- Controlar el acceso con **roles** y **usuarios** (administrador, asignador, empresa de catering, usuario consulta).

Con esta base de datos se cubren todos los flujos de trabajo necesarios para:
1. Diseñar plantillas de menú según dietas y ciclos semanales.  
2. Asignar esos menús a cada residente en desayuno, comida y cena.  
3. Adaptar las asignaciones a alergias y restricciones.  
4. Registrar y auditar cualquier incidencia en el servicio.  
---

## Estructura de la base de datos

- **roles**  
  Define cuatro roles con permisos granulares (administrador, encargado de menús, empresa de catering, usuario de consulta). :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

- **catering**  
  Datos de las empresas proveedoras: nombre, persona de contacto, teléfono y correo. :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}

- **tipos_dieta**  
  Cinco dietas estándar con código, nombre, descripción y fecha de creación. :contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

- **platos**  
  Catálogo de platos: nombre, descripción, ingredientes, referencias a *alergenos*, dietas permitidas y tipo de comida (desayuno, comida, cena). :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

- **alergenos**  
  Lista maestra de alérgenos con `_id`, nombre y descripción. :contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}

- **plantilla_menu**  
  Plantillas cíclicas por dieta y semana, definiendo qué `dishX` se sirve en cada comida de cada día del ciclo. :contentReference[oaicite:12]{index=12}:contentReference[oaicite:13]{index=13}

- **residentes**  
  Registro de residentes con datos demográficos, alergias referenciadas a *alergenos* y dietas asignadas. :contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

- **asignaciones**  
  Historial de asignaciones de menús a residentes, incluyendo quién asignó, cuándo y la empresa de catering responsable. :contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}

- **registro_incidencias**  
  Seguimiento de problemas en el servicio (plato no servido, plato equivocado, retraso, alergeno detectado, plato demasiado caliente), con detalles para cada incidencia. :contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

---

## Uso - Prerrequisitos y Versiones para Clonar y Utilizar el Proyecto

Para seguir este manual, necesitarás tener instalados los siguientes componentes:

A. **MongoDB Server** (versión utilizada: 8.0.6)
   ```bash
   # Verificar instalación
   mongod --version
   ```

B. **MongoDB Shell** (versión utilizada: 2.5.1)
   ```bash
   # Verificar instalación
   mongosh --version
   ```

C. **MongoDB Database Tools** (versión utilizada: 100.9.0)
   ```bash
   # Verificar instalación
   mongodump --version
   ```

   Si no están instaladas las MongoDB Database Tools, puedes instalarlas con:
   ```bash
   wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2204-x86_64-100.9.0.deb
   sudo dpkg -i mongodb-database-tools-ubuntu2204-x86_64-100.9.0.deb

### 1. Iniciar y Configurar el Servicio de MongoDB

Antes de comenzar, asegúrate de que el servicio de MongoDB esté en ejecución:

```bash
# Verificar el estado del servicio
sudo systemctl status mongod

# Si no está en ejecución, iniciarlo
sudo systemctl start mongod

# Configurar para que se inicie automáticamente al reiniciar
sudo systemctl enable mongod

### 2. Explorar la Estructura del Backup

Es importante entender la estructura del backup antes de restaurarlo:

```bash
# Listar los directorios y archivos en el directorio mongodb_export
ls -R mongodb_export/

# Ejemplo de estructura típica:
# mongodb_export/
# └── nombre_base_datos/
#     ├── coleccion1.bson
#     ├── coleccion1.metadata.json
#     ├── coleccion2.bson
#     └── coleccion2.metadata.json
```

### 3. Restaurar la Base de Datos

Utiliza `mongorestore` para importar la base de datos:

```bash
# Ejemplo específico para Residencia_menus
mongorestore --db residencia_menus mongodb_export/residencia_menus
```

### 4. Verificar la Restauración

Confirma que la base de datos se ha restaurado correctamente:

```bash
# Ver todas las bases de datos disponibles
mongosh --eval "db.getMongo().getDBs()"
```

# Conectarse a la base de datos y listar sus colecciones
mongosh
use residencia_menus
show collections
db.residencia_menus.find().limit(5) 

## 5. Acceder a la Base de Datos con MongoDB Compass

1. Abre MongoDB Compass
2. Conéctate usando la URL: `mongodb://localhost:27017`
3. Navega a la base de datos restaurada
4. Explora las colecciones y documentos


## 6. Exportar para poder subir al github


### Ver Todas las Bases de Datos:
``bash
mongosh --eval "db.adminCommand('listDatabases')"

//// Crear Carpeta y Exportar la Base de Datos 
mkdir -p mongodb_export && mongodump --db residencia_menus --out mongodb_export
```

