#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTANTE: Este script debe ejecutarse dentro del entorno virtual:
    source venv/bin/activate
    python export_mongodb_to_json.py
"""
"""
Script para exportar toda la base de datos MongoDB a un único archivo JSON estructurado.
Este script conecta a la base de datos MongoDB, obtiene todas las colecciones
y exporta todos los documentos a un archivo JSON.
"""

import json
import os
from datetime import datetime
from bson import json_util
import pymongo
from pymongo import MongoClient

def connect_to_mongodb(host='localhost', port=27017, db_name='residencia_menus'):
    """
    Conecta a la base de datos MongoDB.

    Args:
        host (str): Host de MongoDB (por defecto: localhost)
        port (int): Puerto de MongoDB (por defecto: 27017)
        db_name (str): Nombre de la base de datos (por defecto: residencia_menus)

    Returns:
        pymongo.database.Database: Objeto de base de datos MongoDB
    """
    try:
        client = MongoClient(host, port)
        db = client[db_name]
        print(f"Conexión exitosa a la base de datos '{db_name}'")
        return db
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        raise

def get_all_collections(db):
    """
    Obtiene todas las colecciones de la base de datos.

    Args:
        db (pymongo.database.Database): Objeto de base de datos MongoDB

    Returns:
        list: Lista de nombres de colecciones
    """
    try:
        collections = db.list_collection_names()
        print(f"Se encontraron {len(collections)} colecciones: {', '.join(collections)}")
        return collections
    except Exception as e:
        print(f"Error al obtener colecciones: {e}")
        raise

def export_to_json(db, output_file='mongodb_export_full.json'):
    """
    Exporta todas las colecciones a un único archivo JSON.

    Args:
        db (pymongo.database.Database): Objeto de base de datos MongoDB
        output_file (str): Ruta del archivo de salida
    """
    try:
        # Crear un diccionario para almacenar todos los datos
        all_data = {
            "database": db.name,
            "exported_at": datetime.now().isoformat(),
            "collections": {}
        }

        # Obtener todas las colecciones
        collections = get_all_collections(db)

        # Para cada colección, obtener todos los documentos
        for collection_name in collections:
            print(f"Exportando colección: {collection_name}")
            collection = db[collection_name]
            documents = list(collection.find())

            # Convertir ObjectId y otros tipos BSON a formato JSON
            all_data["collections"][collection_name] = json.loads(json_util.dumps(documents))

            print(f"  - {len(documents)} documentos exportados")

        # Guardar todo en un archivo JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)

        print(f"\nExportación completada. Archivo guardado como: {output_file}")
        print(f"Tamaño del archivo: {os.path.getsize(output_file) / (1024*1024):.2f} MB")

    except Exception as e:
        print(f"Error durante la exportación: {e}")
        raise

def main():
    """Función principal"""
    try:
        # Parámetros de conexión (pueden ser modificados según sea necesario)
        host = 'localhost'
        port = 27017
        db_name = 'residencia_menus'
        output_file = 'mongodb_export_full.json'

        print("=== Exportador de MongoDB a JSON ===")
        print(f"Conectando a MongoDB ({host}:{port}, base de datos: {db_name})...")

        # Conectar a la base de datos
        db = connect_to_mongodb(host, port, db_name)

        # Exportar a JSON
        export_to_json(db, output_file)

    except Exception as e:
        print(f"Error en la ejecución del script: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
