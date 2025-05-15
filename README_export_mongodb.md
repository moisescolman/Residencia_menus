# Exportador de MongoDB a JSON

Este script permite exportar toda la base de datos MongoDB a un único archivo JSON estructurado. El archivo resultante contendrá todas las colecciones y documentos de la base de datos en un formato JSON bien organizado.

## Requisitos

- Python 3.6 o superior
- Biblioteca PyMongo
- Acceso a la base de datos MongoDB

## Instalación de dependencias

Antes de ejecutar el script, asegúrate de tener instalada la biblioteca PyMongo:

```bash
pip install pymongo
```

## Uso

1. Asegúrate de que el servidor MongoDB esté en ejecución
2. Ejecuta el script:

```bash
python export_mongodb_to_json.py
```

Por defecto, el script:
- Se conecta a MongoDB en `localhost:27017`
- Utiliza la base de datos `residencia_menus`
- Genera un archivo llamado `mongodb_export_full.json` en el directorio actual

## Personalización

Si necesitas modificar los parámetros de conexión o el nombre del archivo de salida, puedes editar las siguientes líneas en la función `main()` del script:

```python
# Parámetros de conexión (pueden ser modificados según sea necesario)
host = 'localhost'
port = 27017
db_name = 'residencia_menus'
output_file = 'mongodb_export_full.json'
```

## Estructura del archivo JSON generado

El archivo JSON generado tendrá la siguiente estructura:

```json
{
  "database": "residencia_menus",
  "exported_at": "2023-06-01T12:34:56.789012",
  "collections": {
    "alergenos": [
      { "_id": "alerg1", "nombre": "Gluten", ... },
      { "_id": "alerg2", "nombre": "Crustáceos", ... },
      ...
    ],
    "residentes": [
      { "_id": "res1", "nombre": "Maria Jesus", ... },
      { "_id": "res2", "nombre": "José", ... },
      ...
    ],
    ...
  }
}
```

## Notas importantes

- El script convierte automáticamente los tipos de datos específicos de MongoDB (como ObjectId) a formatos compatibles con JSON.
- Dependiendo del tamaño de tu base de datos, la exportación puede tardar varios minutos.
- Asegúrate de tener suficiente espacio en disco para el archivo JSON resultante.
